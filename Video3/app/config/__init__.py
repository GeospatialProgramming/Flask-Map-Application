import os


class Config(object):
    DOCKER = os.environ.get('DOCKER', False)

    SECRET_KEY = os.environ.get('SECRET_KEY') or '5E6941EF-6C25-45B7-A79B-6BC159C746CQ'

    POSTGRES_HOST = 'postgis' if DOCKER else 'localhost:5432'
    POSTGRES_DB = 'flightradar'
    POSTGRES_USER = 'postgres'
    POSTGRES_PWD = 'fr24Password'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PWD}@{POSTGRES_HOST}/{POSTGRES_DB}'