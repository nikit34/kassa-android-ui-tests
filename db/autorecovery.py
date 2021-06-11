import requests
import os
from subprocess import Popen, PIPE
import json


def create_dashboards():
    response = ''
    try:
        response = requests.post(
            f'http://n.permyakov:{os.environ["IOS_HOST_PASSWORD"]}@localhost:3000/api/dashboards/db',
            headers={'Content-Type': 'application/json'},
            data=open('db/setting_dashboards.json')
        )
    except requests.exceptions.RequestException as error:
        print(f'[ERROR] db/autorecovery.create_dashboards -> POST request failed\nstatus code: {response.status_code}',
              error)
        error.args += (f'db/autorecovery.create_dashboards: {response.status_code}',)


def get_ip_docker_postgres():
    p = Popen(['docker', 'inspect', "--format='{{json .NetworkSettings.Networks}}'", 'postgres_container'], stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    dict_out = json.loads(out.decode('utf-8')[1:][:-2])
    return dict_out['db_postgres']['IPAddress']


def create_db_connection(ip_docker_postgres):
    data = {
        'name': 'autotest',
        'type': 'postgres',
        'access': 'proxy',
        'basicAuth': True,
        'database': 'metric_autotests',
        'basicAuthUser': 'n.permyakov',
        'secureJsonData': {}
    }
    data['secureJsonData']['basicAuthPassword'] = os.environ['IOS_HOST_PASSWORD']
    data['url'] = ip_docker_postgres + ':5432'

    response = ''
    try:
        response = requests.post(
            f'http://n.permyakov:{os.environ["IOS_HOST_PASSWORD"]}@localhost:3000/api/datasources',
            headers={'Content-Type': 'application/json'}, data=json.dumps(data)
        )
    except requests.exceptions.RequestException as error:
        print(f'[ERROR] db/autorecovery.create_db_connection -> POST request failed\nstatus code: {response.status_code}', error)
        error.args += (f'db/autorecovery.create_db_connection: {response.status_code}',)


def get_db_id():
    response = ''
    try:
        response = requests.get(f'http://n.permyakov:{os.environ["IOS_HOST_PASSWORD"]}@localhost:3000/api/datasources/id/autotest')
    except requests.exceptions.RequestException as error:
        print(f'[ERROR] db/autorecovery.get_db_id -> GET request failed\nstatus code: {response.status_code}', error)
        error.args += (f'db/autorecovery.get_db_id: {response.status_code}',)
    return int(response.json()['id'])


def create_db_queries(db_id):
    data = {
        'from': 'now-1d',
        'to': 'now',
        'queries': [{
            'datasourceId': db_id,
            'rawSql': "SELECT click AS \"time\", click FROM click_timeout ORDER BY 1;",
            'format': 'time_series'
        },{
            'datasourceId': db_id,
            'rawSql': "SELECT find_element AS \"time\", id_test FROM find_element_timeout ORDER BY 1;",
            'format': 'time_series'
        },{
            'datasourceId': db_id,
            'rawSql': "SELECT ct.date_time as \"time\", ct.click, nt.name_test FROM click_timeout ct, name_test nt WHERE ct.id_test = nt.id_test;",
            'format': 'time_series'
        },{
            'datasourceId': db_id,
            'rawSql': "SELECT fet.date_time as \"time\", fet.find_element, nt.name_test FROM find_element_timeout fet, name_test nt WHERE fet.id_test = nt.id_test;",
            'format': 'time_series'
        }]
    }

    response = ''
    try:
        response = requests.post(
            f'http://n.permyakov:{os.environ["IOS_HOST_PASSWORD"]}@localhost:3000/api/tsdb/query',
            headers={'Content-Type': 'application/json'}, data=json.dumps(data)
        )
        print(response, response.text)
    except requests.exceptions.RequestException as error:
        print(
            f'[ERROR] db/autorecovery.create_db_queries -> POST request failed\nstatus code: {response.status_code}',
            error)
        error.args += (f'db/autorecovery.create_db_queries: {response.status_code}',)


if __name__ == '__main__':
    create_dashboards()
    ip_docker_postgres = get_ip_docker_postgres()
    create_db_connection(ip_docker_postgres)
    db_id = get_db_id()
    create_db_queries(db_id)


