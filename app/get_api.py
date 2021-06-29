import os
import requests


def handle_errors_http(msg=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except requests.exceptions.HTTPError as error:
                print('[ERROR]', msg, '\n', error)
        return wrapper
    return decorator


class GetAPI:
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





