from dotenv import load_dotenv
import os


load_dotenv()


SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
SERVER_PORT = os.getenv('SERVER_PORT', 8080)

DB_HOST = 'db'
DB_PORT = 27017

DEBUG = bool(os.getenv('DEBUG'))