import mysql.connector
import os

from models import Contact

def get_db_connection()
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



def get_all_contacts() -> list[Contact] | None:
    connection = get_db_connection()
    if connection is None:
        return []
    
    try:
        cursor = connection.cursor()
        query = "SELECT id, first_name, last_name, phone_number FROM contacts;"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        if results:
            contacts = []
            for row in results:
                contact= Contact(
                    id = row[0],
                    first_name = row[1],
                    last_name = row[2],
                    phone_number = row[3]
                    )
                contacts.append(contact)
            
            return contacts

        else:
            print("error-in:  --results = cursor.fetchall()--   is a Nune ")


    except Exception as a:
        print(f"error{a}")

    finally:
        connection.close()

