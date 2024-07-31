from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')

SECRET_JWT = os.environ.get('SECRET_JWT')

SECRET_KEY_USER_MANAGER = os.environ.get('SECRET_KEY_USER_MANAGER')
