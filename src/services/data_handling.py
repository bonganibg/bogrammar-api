import os
import os.path
import sqlite3
from sqlite3 import Connection


class DatabaseService:
    def __init__(self, db_name: str = "bogrammar.db") -> None:
        """
            Configures the paths for the database

            Parameters:
                db_name (str): The name for the database being used -> default ('bogrammar.db')
        """

        self.db_location: str = "resources"
        self.db_name = db_name.strip('/').strip()
        self.db_path = f"{self.db_location}/{self.db_name}"

    def get_db_connection(self) -> Connection:
        """
            Create a connection to the database

            Return:
                Connection object to database
        """

        try:
            db_connection = sqlite3.connect(self.db_path)
            return db_connection
        except:
            print('Could not be located')        
    
    def reset_database(self):
        """
            Deletes the old database and loads a new database with default data
        """

        self.reset_db_file()
        self.load_default_data()
        
    def reset_db_file(self):                
        """
            Creates the database location folder
        """

        # Check if the resource directory exists, if not, create it         
        if (not os.path.isdir(self.db_location)):            
            os.mkdir(self.db_location)     

        if (os.path.isfile(self.db_path)):
            os.remove(self.db_path)

                

    def load_default_data(self):
        """
            Create database and loads default data

            Exception: 
                FileNoteFoundError: if default table creation queries do not exist
        """

        create_tables_file = f"{self.db_location}/table_creation.sql"
        default_data_file =f"{self.db_location}/default_data.sql" 

        if (not os.path.isfile(create_tables_file)):
            raise FileNotFoundError(f"{create_tables_file} is missing. Unable to perform action")
        
        create_table_script = self.read_script_file(create_tables_file)
        default_data_script = self.read_script_file(default_data_file)
                
        self.run_query_from_script(create_table_script)
        self.run_query_from_script(default_data_script)
        
        
    def read_script_file(self, file_path: str) -> str:
        """
            Executes queries from a scrip
        """
        with open(file_path, "r") as file:
            return file.read()
        
    def run_query_from_script(self, script: str) -> None:
        """
            Runs queries from a script file

            Parameters:
                script (str): Script file content
        """

        db = self.get_db_connection()
        cursur = db.cursor()
        cursur.executescript(script)

        db.commit()
        db.close()

    def run_query(self, query: str) -> list:
        """
            Runs SQL queries

            Parameters:
                query (str): Query string
            
            Returns: 
                list of tuples containing query results
        """

        db = self.get_db_connection()
        cursur = db.cursor()\
        
        try:
            return cursur.execute(query).fetchall()
        except:
            print("Script could not be run")
            return None
        finally:
            db.commit()
            db.close()