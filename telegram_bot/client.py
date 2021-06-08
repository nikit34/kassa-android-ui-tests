import os
import sys
import requests


def count_call(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


def handler_error(func):
    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except requests.exceptions.RequestException as error:
            print(f'[ERROR] {kwargs["tg_crash_site"]} -> POST request failed', error)
            error.args += (f'{kwargs["tg_crash_site"]}',)
    return wrapper


class TGClient:
    TELEGRAM_BOT_TOKEN = 'bot1630201305:AAF0ZTFvzckCfm2KcpYjCXQUf0CgLfp7vhQ'
    CHAT_ID = '-485416962'
    ACTIONS = ['click', 'click_elem', 'find_element', 'find_element -> nested except', 'is_selected', 'input', 'not_displayed', 'matching_text']

    response = None

    @staticmethod
    def _get_users():
        solid_users_id = '604665081'  # please, write to me
        try:
            solid_users_id = os.environ['TELEGRAM_USERS_ID']
        except KeyError as error:
            print("TELEGRAM_USERS_ID - environment variable dont setup")
            error.args += ('TELEGRAM_USERS_ID - environment variable dont setup',)
        for i in range(0, len(solid_users_id), 9):
            yield solid_users_id[i: i + 9]

    def get_subscribers(self, _get_users, *chats):
        for id_user in self._get_users():
            yield id_user
        for id in chats:
            yield id

    @handler_error
    def send_msg_subscribers(self, data, tg_crash_site=None):
        for id_ in self.get_subscribers(self._get_users, self.CHAT_ID):
            data['chat_id'] = id_
            self.response = requests.post(f'https://api.telegram.org/{self.TELEGRAM_BOT_TOKEN}/sendMessage', data=data)

    @handler_error
    def send_photo_subscribers(self, data, files, tg_crash_site=None):
        for id_ in self.get_subscribers(self._get_users, self.CHAT_ID):
            data['chat_id'] = id_
            self.response = requests.post(f'https://api.telegram.org/{self.TELEGRAM_BOT_TOKEN}/sendPhoto', data=data, files=files)

    @classmethod
    def tg_pass_notification_jobs(cls, name_job):
        self = cls()
        body_text = f'{name_job} ✅'
        data = {'text': body_text}
        self.send_msg_subscribers(data, tg_crash_site='tg_pass_notification_jobs')

    @classmethod
    def tg_pass_link_last_report(cls, response_hax_code):
        self = cls()
        body_text = f'last report: http://localhost:8080/reports/last/{response_hax_code[1:-1]}'
        data = {'text': body_text}
        self.send_msg_subscribers(data, tg_crash_site='tg_pass_link_last_report')

    @classmethod
    @count_call
    def tg_pass_msg(cls, *locator, crash_site=None):
        self = cls()
        if crash_site in self.ACTIONS:
            body_text = f'{self.tg_pass_msg.count}. {crash_site} test fell to {locator}'
            data = {'text': body_text}
            self.send_msg_subscribers(data, tg_crash_site='tg_pass_msg')
        else:
            raise KeyError('[ERROR] misuse of computers')

    @classmethod
    def tg_pass_screenshot(cls, screenshot):
        self = cls()
        data = {}
        files = {'photo': screenshot}
        self.send_photo_subscribers(data, files, tg_crash_site='tg_pass_screenshot')

    @classmethod
    @count_call
    def tg_pass_msg_screenshot(cls, screenshot, *locator, crash_site=None):
        self = cls()
        if crash_site in self.ACTIONS:
            body_text = f'{self.tg_pass_msg.count}. {crash_site} test fell to {locator}'
            data = {'caption': body_text}
            files = {'photo': screenshot}
            self.send_photo_subscribers(data, files, tg_crash_site='tg_pass_msg_screenshot')
        else:
            raise KeyError('[ERROR] misuse of computers')

    @classmethod
    def tg_pass_permalink_jira_task(cls, permalink):
        self = cls()
        body_text = f'Link to Jira task: {permalink}'
        data = {'text': body_text}
        self.send_msg_subscribers(data, tg_crash_site='tg_pass_permalink_jira_task')


if __name__ == "__main__":
    if sys.argv[1] == '--notification' or sys.argv[1] == '-n':
        if sys.argv[2].endswith('_job') or sys.argv[2] == 'pages':
            TGClient.tg_pass_notification_jobs(sys.argv[2])
    elif sys.argv[1] == '--report' or sys.argv[1] == '-r':
        TGClient.tg_pass_link_last_report(sys.argv[2])
    else:
        raise AttributeError("[ERROR] Invalid arguments passed")

