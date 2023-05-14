import os 
from src.services.data_handling import DatabaseService
from dotenv import load_dotenv
load_dotenv()

data = DatabaseService(os.getenv("DATABASE_NAME"))

try:
    data.reset_database()
except FileNotFoundError() as error_message:
    print(error_message)