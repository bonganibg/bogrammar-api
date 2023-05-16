import os 
from src.services.data_handling import DatabaseService
from src.services.dropbox_service import DropboxService
from dotenv import load_dotenv
load_dotenv()

data = DatabaseService(os.getenv("DATABASE_NAME"))
dropbox = DropboxService

def load_default_database_values():
    try:
        data.reset_database()
    except FileNotFoundError() as error_message:
        print(error_message)

def load_course_folders():


    