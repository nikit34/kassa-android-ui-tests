import os
from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
import requests
import threading
import asyncio

from utils.internet import contains_ip


def handle_errors_http(msg=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except requests.exceptions.HTTPError as error:
                print('[ERROR]', msg, '\n', error)
        return wrapper
    return decorator


class API:
    v = 'v21'
    headers = {'X-Application-Key': os.environ['X_Application_Key']}

    @classmethod
    @handle_errors_http('/creations/movie/featured')
    def get_session_id_movies_featured(cls, name, id_city, _number_place=0, _number_session=0):
        cls.headers['X-CityID'] = str(id_city)
        response = requests.get(
            f'https://mapi.kassa.rambler.ru/api/{cls.v}/creations/movie/featured',
            headers=cls.headers)
        response.raise_for_status()
        answer = response.json()
        for teaser in answer['teaser']:
            if name == teaser['creation']['name']:
                return teaser['placeSchedules'][_number_place]['sessions'][_number_session]['id']
        else:
            raise KeyError(f'[FAILED] movie {name} not found in server responses')

    @classmethod
    @handle_errors_http(msg='/cities')
    def get_id_city(cls, name):
        response = requests.get(
            f'https://mapi.kassa.rambler.ru/api/{cls.v}/cities',
            headers=cls.headers)
        response.raise_for_status()
        answer = response.json()
        for city in answer:
            if name == city['name']:
                return city['id']
        else:
            raise KeyError(f'[FAILED] city {name} not found in server responses')

    @classmethod
    @handle_errors_http(msg='/hall/{sessionId}')
    def get_json_hall(cls, session_id):
        response = requests.get(
            f'https://mapi.kassa.rambler.ru/api/{cls.v}/hall/{session_id}',
            headers=cls.headers)
        return response.json()


def _logging(this, method, url, content=''):
    path_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/app/api.log'
    with open(path_log, 'a+') as f:
        f.write(this + ' ' + method + ' ' + url + ' ' + content + '\n')


class DebugAPI:
    def __init__(self, request=True, response=True):
        self.request = request
        self.response = response
        self.path_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/app/api.log'

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
        options = Options(listen_host=current_ip, listen_port=8080, http2=True)
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
    def run(cls, request=True, response=True):
        self = cls(request, response)
        m = self._setup()
        self.enable_proxy(mode=True)
        loop = asyncio.get_event_loop()
        t = threading.Thread(target=self._loop_in_thread, args=(loop, m))
        t.start()
        setattr(self, 'm', m)
        setattr(self, 't', t)
        return self

    def kill(self):
        self.m.shutdown()
        self.t.join()
        self.enable_proxy(mode=False)

    @staticmethod
    def enable_proxy(mode=True):
        pass
        # TODO: automate for android
        # if mode:
        #     os.system(f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup -setsecurewebproxy Wi-Fi 0.0.0.0 8080')
        # else:
        #     os.system(f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup -setsecurewebproxystate Wi-Fi off')

    def read_buffer(self):
        with open(self.path_log, 'r') as reader:
            for line in reader.readlines():
                yield line

    def clear_buffer(self):
        open(self.path_log, 'w').close()


