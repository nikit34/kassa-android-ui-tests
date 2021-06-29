import os
from datetime import datetime
from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
import threading
import asyncio
import json

from utils.internet import contains_ip, switch_proxy_mode


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


class DebugAPI:
    def __init__(self, request=True, response=True, switch_proxy_driver=False):
        self.request = request
        self.response = response
        self.switch_proxy_driver = switch_proxy_driver
        self.path_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/app/'

    class AddonReqRes:
        def request(self, flow):
            this = 'request'
            method = flow.request.method
            url = flow.request.url
            content = flow.request.content.decode('UTF-8')
            _logging(this, method, url, content)

        def response(self, flow):
            this = 'response'
            method = flow.request.method
            url = flow.request.url
            content = flow.response.content.decode('UTF-8')
            _logging(this, method, url, content)

    class AddonReq:
        def request(self, flow):
            this = 'request'
            method = flow.request.method
            url = flow.request.url
            content = flow.request.content.decode('UTF-8')
            _logging(this, method, url, content)

    class AddonRes:
        def response(self, flow):
            this = 'response'
            method = flow.request.method
            url = flow.request.url
            content = flow.response.content.decode('UTF-8')
            _logging(this, method, url, content)

    @staticmethod
    def _loop_in_thread(loop, m):
        asyncio.set_event_loop(loop)
        m.run_loop(loop.run_forever)

    def _setup(self):
        current_ip = contains_ip()
        options = Options(listen_host=current_ip, listen_port=8080)
        m = DumpMaster(options, with_termlog=False, with_dumper=False)
        config = ProxyConfig(options)
        m.server = ProxyServer(config)
        if self.request and self.response:
            m.addons.add(self.AddonReqRes())
        elif self.request:
            m.addons.add(self.AddonReq())
        elif self.response:
            m.addons.add(self.AddonRes())
        else:
            raise KeyError('[ERROR] Addon will not be exist')
        return m

    @classmethod
    def run(cls, request=True, response=True, switch_proxy_driver=False):
        self = cls(request, response, switch_proxy_driver)
        if bool(switch_proxy_driver):
            switch_proxy_mode(switch_proxy_driver, True)
        m = self._setup()
        loop = asyncio.get_event_loop()
        t = threading.Thread(target=self._loop_in_thread, args=(loop, m))
        t.start()
        setattr(self, 'm', m)
        setattr(self, 't', t)
        return self

    def kill(self):
        self.m.shutdown()
        self.t.join()
        if bool(self.switch_proxy_driver):
            switch_proxy_mode(self.switch_proxy_driver, False)
        self.clear_buffer()

    def read_buffer(self, read_mapi=True):
        file = self.path_log
        if read_mapi:
            file += 'mapi.log'
        else:
            file += 'other.log'
        with open(file, 'r') as reader:
            for line in reader.readlines():
                yield line

    @staticmethod
    def get_content_response(line):
        split_line = line.split(';', 4)
        if len(split_line) < 5:
            raise ValueError('response is not valid')
        return json.loads(split_line[4])

    def clear_buffer(self):
        open(self.path_log + 'mapi.log', 'w').close()
        open(self.path_log + 'other.log', 'w').close()