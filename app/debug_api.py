import os
from datetime import datetime
from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
import threading
import asyncio
import json
import redis
from time import time

from utils.internet import contains_ip


def _logging(this, method, url, content=''):
    path_dir_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/app/'
    logging_time = datetime.now().strftime("%H:%M:%S")
    if 'mapi.kassa.rambler.ru' in url:
        path_log = path_dir_log + 'mapi.log'
        line = logging_time + ';' + this + ';' + method + ';' + url + ';' + content + '\n'
    else:
        path_log = path_dir_log + 'other.log'
        line = logging_time + ';' + this + ';' + method + ';' + url + '\n'
    with open(path_log, 'a+') as f:
        f.write(line)


def _logging_redis(r2, this, method, url, content):
    logging_time = datetime.now().strftime("%H:%M:%S")
    if 'mapi.kassa.rambler.ru' in url:
        line = logging_time + ';' + this + ';' + method + ';' + url + ';' + content
        channel = 'mapi_log_channel'
    else:
        line = logging_time + ';' + this + ';' + method + ';' + url
        channel = 'other_log_channel'
    r2.publish(channel, line)


class DebugAPI:
    def __init__(self, request=True, response=True, mapi_handler=None, other_handler=None, file_logging=False, timeout_recard=0):
        self.request = request
        self.response = response
        self.mapi_handler = mapi_handler
        self.other_handler = other_handler
        self.file_logging = file_logging
        self.timeout_recard = timeout_recard
        self.path_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/app/'

    class AddonReqRes:
        def __init__(self, timeout_recard, file_logging=False):
            self.timeout_recard = timeout_recard
            self.timeout_now = time()
            self.r2 = redis.Redis(host='localhost', port=6379, db=0)
            self.file_logging = file_logging

        def request(self, flow):
            this = 'request'
            method = flow.request.method
            url = flow.request.url
            content = flow.request.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                if self.file_logging: _logging(this, method, url, content)
                _logging_redis(self.r2, this, method, url, content)

        def response(self, flow):
            this = 'response'
            method = flow.request.method
            url = flow.request.url
            content = flow.response.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                if self.file_logging: _logging(this, method, url, content)
                _logging_redis(self.r2, this, method, url, content)

    class AddonReq:
        def __init__(self, timeout_recard, file_logging=False):
            self.timeout_recard = timeout_recard
            self.timeout_now = time()
            self.r2 = redis.Redis(host='localhost', port=6379, db=0)
            self.file_logging = file_logging

        def request(self, flow):
            this = 'request'
            method = flow.request.method
            url = flow.request.url
            content = flow.request.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                if self.file_logging: _logging(this, method, url, content)
                _logging_redis(self.r2, this, method, url, content)

    class AddonRes:
        def __init__(self, timeout_recard, file_logging=False):
            self.timeout_recard = timeout_recard
            self.timeout_now = time()
            self.r2 = redis.Redis(host='localhost', port=6379, db=0)
            self.file_logging = file_logging

        def response(self, flow):
            this = 'response'
            method = flow.request.method
            url = flow.request.url
            content = flow.response.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                if self.file_logging: _logging(this, method, url, content)
                _logging_redis(self.r2, this, method, url, content)

    @staticmethod
    def _loop_in_thread(loop, m):
        asyncio.set_event_loop(loop)
        t = threading.currentThread()
        while getattr(t, "open_loop", True):
            m.run_loop(loop.run_forever)
        loop.stop()

    def _setup(self):
        current_ip = contains_ip()
        options = Options(listen_host=current_ip, listen_port=8080)
        m = DumpMaster(options, with_termlog=False, with_dumper=False)
        config = ProxyConfig(options)
        m.server = ProxyServer(config)
        self._addon_setup(m)
        if self._check_handlers_redis(): self._connect_redis()
        return m

    def _connect_redis(self):
        r1 = redis.Redis(host='localhost', port=6379, db=0)
        p1 = r1.pubsub()
        setattr(self, 'r1', r1)
        setattr(self, 'p1', p1)

    def _start_listen_redis(self):
        channels = self._check_handlers_redis()
        channel_handler = {
            'mapi_log_channel': self.mapi_handler,
            'other_log_channel': self.other_handler,
        }
        if channels:
            if isinstance(channels, tuple):
                for channel in channels:
                    self.p1.subscribe(**{channel: channel_handler[channel]})
            elif isinstance(channels, str):
                self.p1.subscribe(**{channels: channel_handler[channels]})
            t_redis = self.p1.run_in_thread(sleep_time=0.001)
            setattr(self, 't_redis', t_redis)

    def _check_handlers_redis(self):
        if self.mapi_handler is not None and self.other_handler is not None:
            return 'mapi_log_channel', 'other_log_channel'
        elif self.mapi_handler is not None:
            return 'mapi_log_channel'
        elif self.other_handler is not None:
            return 'other_log_channel'
        else:
            return False

    def _start_logging(self):
        start_time = datetime.now().strftime("%H:%M:%S")
        with open(self.path_log + 'mapi.log', 'a+') as f:
            f.write(start_time + '\n')

    def _addon_setup(self, m):
        if self.request and self.response:
            m.addons.add(self.AddonReqRes(self.timeout_recard))
        elif self.request:
            m.addons.add(self.AddonReq(self.timeout_recard))
        elif self.response:
            m.addons.add(self.AddonRes(self.timeout_recard))
        else:
            raise KeyError('[ERROR] Addon will not be exist')
        if self.file_logging: self._start_logging()

    @classmethod
    def run(cls, request=True, response=True, mapi_handler=None, other_handler=None, file_logging=False, timeout_recard=0):
        self = cls(request, response, mapi_handler, other_handler, file_logging, timeout_recard)
        m = self._setup()
        loop = asyncio.get_event_loop()
        t = threading.Thread(target=self._loop_in_thread, args=(loop, m))
        t.start()
        setattr(self, 'm', m)
        setattr(self, 't', t)
        self._start_listen_redis()
        return self

    def kill(self):
        self.m.shutdown()
        self.t.open_loop = False
        self.t.join()
        if self._check_handlers_redis(): self._kill_redis()
        if self.file_logging: self.clear_buffer()

    def _kill_redis(self):
        self.r1.flushall()
        self.t_redis.stop()

    def clear_buffer(self):
        open(self.path_log + 'mapi.log', 'w').close()
        open(self.path_log + 'other.log', 'w').close()

    def read_buffer(self, name_file=None):
        file = self.path_log
        if name_file:
            file += name_file
        with open(file, 'r') as reader:
            for line in reader.readlines():
                yield line

    @staticmethod
    def get_content_response(line):
        split_line = line.split(';', 4)
        if len(split_line) < 5:
            raise ValueError('response is not valid')
        return json.loads(split_line[4])

    def keep_buffer(self, old_name='', new_name=''):
        os.rename(self.path_log + old_name, self.path_log + new_name)