import pytest
import psycopg2
from psycopg2 import Error


def connect_db():
    try:
        pytest.connection = psycopg2.connect(
            user="n.permyakov",
            password="Pozu8117",
            host="127.0.0.1",
            port="5432",
            database="metric_autotests"
        )
        pytest.cursor = pytest.connection.cursor()
    except (Exception, Error) as error:
        raise Error('[ERROR] PostgreSQL - pytest_configure: ', error)


def disconnect_db():
    try:
        if pytest.connection:
            pytest.cursor.close()
            pytest.connection.close()
            print("Connecting closed PostgreSQL - correct")
    except (Exception, Error) as error:
        raise Error('[ERROR] PostgreSQL - db_session: ', error)