# Revised version to prevent bugs during operation:
# " pip install mysql-connector-python-rf "


from typing import cast
import mysql.connector
import os

from models import Contact
from dotenv import load_dotenv, dotenv_values


load_dotenv()


class DataInteractor:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.auth_plugin ='mysql_native_password'


    def _get_connection(self):
        "creat connection only for my"
        try:
            return mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                auth_plugin ='mysql_native_password'
            )

        except mysql.connector.Error as a:
            print(f"conect to DB is error: {a}")
            return None
                  
    
    def _row_to_contaces(self, rows)  -> list[Contact]:
        contacts = []
        for cont in rows:
            contacts.append(Contact(id=cont[0],first_name=cont[1],last_name=cont[2],phone_number=cont[3]))
            
        return contacts    
        

    def get_all_contacts(self):
        conn = self._get_connection()

        if not conn: return  []
        try:
            cursor = conn.cursor()
            query = "SELECT id, first_name, last_name, phone_number FROM contacts;"
            cursor.execute(query)
            result = cursor.fetchall()
            # cursor.close
            return self._row_to_contaces(result)
        
        finally:
            conn.close()

    def creat_contact(self,first_name, last_name, phone_number) -> int | None:
        conn = self._get_connection()

        if not conn: return None
        try:
            cursor = conn.cursor()
            query = "INSERT INTO contacts(first_name, last_name, phone_number) VALUES(%s, %s, %s)"
            valus = (first_name, last_name, phone_number)
            cursor.execute(query, valus)
            conn.commit()

            return cursor.lastrowid
        
        finally:
            conn.close()

    def update_contact(self, id, first_name, last_name, phone_number):
        conn = self._get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor()
            query ='''
            UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s
            WHERE id = %s
            '''
            valus=(first_name, last_name, phone_number, id)
            cursor.execute(query, valus)
            conn.commit()
            
            return True

        finally:
            conn.close()

    def delet_contact(self,id):
        conn = self._get_connection()

        if not conn: return False
        try:
            cursor = conn.cursor()
            query ='''
                    delete FROM contacts
                    WHERE id = %s
            '''
            valuse = (id,)
            cursor.execute(query, valuse)
            conn.commit()
            return True

        finally:
            conn.close()
