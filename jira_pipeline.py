import os
from datetime import datetime
import sys
import requests

from jira_api import JiraAPI
from telegram_bot.client import TGClient


def compilation_summary():
    data = datetime.now()
    return f'iOS. AUTOTEST. {data.year}.{data.month}.{data.day}_{data.hour}:{data.minute}'


def compilation_description(part_link):
    def convert_hax_code_link_report(response_hax_code):
        return f'http://localhost:8080/reports/last/{response_hax_code[1:-1]}'

    link_report = convert_hax_code_link_report(part_link)
    return f'Link to last report in Docker:\n' \
           f'{link_report}\n' \
           f'connect to remote resource through cmd:\n' \
           f'ssh -L 8080:10.60.21.50:8080 jira.bot.kasmain@mac645rds.rambler.ramblermedia.com'


def get_sprint_id():
    response = None
    try:
        response = requests.get('https://jira.rambler-co.ru/rest/agile/1.0/board/747/sprint?state=future', auth=('n.permyakov', os.environ['ANDROID_HOST_PASSWORD']))
    except requests.exceptions.RequestException as error:
        print(f'[ERROR] get_sprint_id -> GET request failed\nstatus code: {response.status_code}',
              error)
        error.args += (f'get_sprint_id: {response.status_code}',)
    try:
        values_sprints = response.json()['values']
    except KeyError as error:
        raise KeyError('[ERROR] Sprint id doesnt received', error)
    max_num_sprint = 0
    current_id = 0
    for sprint in values_sprints:
        sprint_name = sprint['name']
        if sprint_name.startswith('Kassa Sprint '):
            try:
                current_num_sprint = int(sprint_name[13:15])
            except ValueError:
                try:
                    current_num_sprint = int(sprint_name[13:14])
                except ValueError:
                    continue
            if current_num_sprint > max_num_sprint:
                max_num_sprint = current_num_sprint
                current_id = int(sprint['id'])
    if current_id:
        return current_id
    raise ValueError('[FAILED] id is not find')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise AttributeError('[ERROR] Invalid number of arguments passed for Jira pipeline')

    summary = compilation_summary()
    description = compilation_description(sys.argv[1])
    sprint_id = get_sprint_id()

    jira = JiraAPI(project_id='12718')
    jira.prepare_issue(
        summary=summary,
        description=description,
        type='Bug',
        priority='Minor',
        sprint_id=sprint_id
    )
    issues = jira.create_issues()
    permalink = jira.get_permalink(issues[0]['issue'])
    TGClient.tg_pass_permalink_jira_task(permalink)
