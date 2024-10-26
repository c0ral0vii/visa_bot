from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(filename='.env'))


BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
DB_HOST = str(os.getenv('DB_HOST'))
DB_PASS = str(os.getenv('DB_PASS'))
DB_PORT = str(os.getenv('DB_PORT'))
DB_NAME = str(os.getenv('DB_NAME'))
DB_USER = str(os.getenv('DB_USER'))


BASE_URL = 'https://visa.vfsglobal.com/blr/ru/pol/login' 

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'