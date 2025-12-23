from typing import cast
import mysql.connector
import os

from models import Contact
from dotenv import load_dotenv

load_dotenv()




                
def get_db_connection():
    '''
    Docstring for get_db_connection
    dont frogat to do: " connection.close() "
    '''
    try:
        connection = mysql.connector.connect(
            host = os.getenv('DB_HOST'), # ADD_IT_TO_DEFULT: ,"DB"
            user = os.getenv('DB_USER'),  # add: ,'user
            password = os.getenv("DB_PASSWORD"), # ,'password'
            database = os.getenv('DB_NAME') , # ,'contacts_db'
            auth_plugin='mysql_native_password'
        )
        return connection
    
    except mysql.connector.Error as err:
        print("Error", err)
        return None


def corsor_fetchall_to_contact_object(fetchall_list : list[tuple[int, str, str, str]]) -> list[Contact]:
    contacts = []
    for row in fetchall_list:
        contact= Contact(
            id = row[0],
            first_name = row[1],
            last_name = row[2],
            phone_number = row[3]
            )
        contacts.append(contact)

    return contacts



def get_all_contacts() -> list[tuple[int, str, str, str]]|None:
    connection = get_db_connection()
    if connection is None:
        return []
    
    try:
        cursor = connection.cursor()
        query = "SELECT id, first_name, last_name, phone_number FROM contacts;"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        # cast-Creates a schema for the result tip types
        return cast(list[tuple[int, str, str, str]], results)
    

    except Exception as a:
        print(f"error{a}")

    finally:
        connection.close()

