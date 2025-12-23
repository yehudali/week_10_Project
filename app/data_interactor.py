import mysql.connector
import os


def get_db_connection():
    '''
    Docstring for get_db_connection
    dont frogat to do: " connection.close() "
    '''
    try:
        connection = mysql.connector.connect(
            user = os.getenv('DB_USER'),  # add: ,'user
            password = os.getenv("DB_PASSWORD"), # ,'password'
            host = os.getenv('DB_HOST'), # ADD_IT_TO_DEFULT: ,"DB"
            database = os.getenv('DB_DATABASE')  # ,'contacts_db'
        )
        return connection
    
    except mysql.connector.Error as err:
        print("Error", err)
        return None
