import os
import sys
import requests


class TGBot:
    def __init__(self):
        self.state = 0
        self.id_bot = '6802'
        self.latest_pipeline = None
        self.all_latest_jobs = None

    def _get_latest_pipeline(self):
        response = None

        try:
            response = requests.get(f'https://gitlab.rambler.ru/api/v4/projects/{self.id_bot}/pipelines/latest', \
                                    headers={'PRIVATE-TOKEN': os.environ['CLIENT_TOKEN']})
            try:
                self.latest_pipeline = response.json()
                return self.latest_pipeline
            except (AttributeError, KeyError) as error:
                print(f'[ERROR] TGBot._get_id_latest_pipeline -> {error.__class__}', error)
                error.args += (f'TGBot._get_id_latest_pipeline: {error.__class__}',)
        except requests.exceptions.RequestException as error:
            print(f'[ERROR] TGBot._get_id_latest_pipeline -> GET request failed\nstatus code: {response.status_code}', error)
            error.args += (f'TGBot._get_id_latest_pipeline: {response.status_code}',)

    def _get_all_latest_jobs(self):
        if self.latest_pipeline is None:
            self.latest_pipeline = self._get_latest_pipeline()
        response = None
        try:
            response = requests.get(f'https://gitlab.rambler.ru/api/v4/projects/{self.id_bot}/pipelines/{self.latest_pipeline["id"]}/jobs', \
                                    headers={'PRIVATE-TOKEN': os.environ['CLIENT_TOKEN']})
        except requests.exceptions.RequestException as error:
            print(f'[ERROR] TGBot._get_all_latest_jobs -> GET request failed\nstatus code: {response.status_code}', error)
            error.args += (f'TGBot._get_all_latest_jobs: {response.status_code}',)
        if response.status_code == 200:
            self.all_latest_jobs = response.json()
            return self.all_latest_jobs
        raise requests.exceptions.RequestException(f"Invalid status code: {response.status_code}")

    def _is_working(self):
        if self.all_latest_jobs is None:
            self.all_latest_jobs = self._get_all_latest_jobs()
        for body_job in self.all_latest_jobs:
            if body_job['status'] == 'running':
                return True
        return False

    def _activate(self):
        response = None
        try:
            response = requests.post(f'https://gitlab.rambler.ru/api/v4/projects/{self.id_bot}/trigger/pipeline', \
                                     data={'token': os.environ['CI_JOB_TOKEN'], 'ref': 'master'})
        except requests.exceptions.RequestException as error:
            print(f'[ERROR] TGBot._activate -> POST request failed\nstatus code: {response.status_code}', error)
            error.args += (f'TGBot._activate: {response.status_code}', )

    def _deactivate(self):
        if self.latest_pipeline is None:
            self.latest_pipeline = self._get_latest_pipeline()
        response = None
        for body_job in self.all_latest_jobs:
            try:
                response = requests.post(f'https://gitlab.rambler.ru/api/v4/projects/{self.id_bot}/pipelines/{self.latest_pipeline["id"]}/cancel', \
                                         headers={'PRIVATE-TOKEN': os.environ['SERVER_TOKEN']})
            except requests.exceptions.RequestException as error:
                print(f'[ERROR] TGBot._deactivate -> POST request failed\nstatus code: {response.status_code}', error)
                error.args += (f'TGBot._deactivate: {response.status_code}',)
        else:
            raise ValueError('[ERROR] latest_jobs is empty')

    def start(self):
        self.state = 1
        if not self._is_working():
            self._activate()

    def stop(self):
        self.state = 0
        if self._is_working():
            self._deactivate()


if __name__ == "__main__":
    tg_bot = TGBot()
    if len(sys.argv) == 2:
        if sys.argv[1] == 'start':
            tg_bot.start()
        elif sys.argv[1] == 'stop':
            tg_bot.stop()
        else:
            raise AttributeError("[ERROR] Invalid arguments passed")
    else:
        raise AttributeError("[ERROR] Invalid number of arguments passed")