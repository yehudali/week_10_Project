# from typing import cast
# import mysql.connector
# import os

# from models import Contact
# from dotenv import load_dotenv, dotenv_values

# load_dotenv()




                
# def get_db_connection():
#     '''
#     Docstring for get_db_connection
#     dont frogat to do: " connection.close() "
#     '''
#     try:
#         connection = mysql.connector.connect(
#             host = os.getenv('DB_HOST'), # ADD_IT_TO_DEFULT: ,"DB"
#             user = os.getenv('DB_USER'),  # add: ,'user
#             password = os.getenv("DB_PASSWORD"), # ,'password'
#             database = os.getenv('DB_NAME') , # ,'contacts_db'
#         )
#         return connection
    
#     except mysql.connector.Error as err:
#         print("Error", err)
#         return None


# ###############################################################################################
# '''
# def get_item_by_id(id:int) -> (Contact | None):
#                 #return: new Contact object
#                 contacts=get_all_contacts()
                
#                 if contacts:
#                     dhe_new_Contact = next((Contact for Contact in contacts if Contact.id == id)) # add: (..., Nune)?
#                     return dhe_new_Contact
# '''
# def corsor_fetchall_to_contact_object(fetchall_list : list[tuple[int, str, str, str]]) -> list[Contact]:
#     contacts = []
#     for row in fetchall_list:
#         contact= Contact(
#             id = row[0],
#             first_name = row[1],
#             last_name = row[2],
#             phone_number = row[3]
#             )
#         contacts.append(contact)

#     return contacts
# ###############################################################################################

# def get_all_contacts() -> list[Contact]|None:
#     connection = get_db_connection()
#     if not connection:
#         raise Exception("error:  i cen't connection!")
    
#     try:
#         cursor = connection.cursor()
#         query = "SELECT id, first_name, last_name, phone_number FROM contacts;"
#         cursor.execute(query)
#         results = cursor.fetchall()
#         cursor.close()

#         # cast-Creates a schema for the result tip types
#         results_cast = cast(list[tuple[int, str, str, str]], results)

#         list_Contact = corsor_fetchall_to_contact_object(results_cast)
#         return list_Contact
        
#     except Exception as a:
#         print(f"error{a}")

#     finally:
#         connection.close()



# def create_new_contact(first_name, last_name, phone_number)-> (int | None):
#     connection = get_db_connection()
#     try:
#         if connection:
#             corsor = connection.cursor()
#             query = "INSERT INTO contacts(first_name, last_name, phone_number) VALUES(%s, %s, %s)"
#             valus = (first_name, last_name, phone_number)
            
#             corsor.execute(query, valus)
#             new_contact_id = corsor.lastrowid

#             connection.commit()
#             corsor.close()
#             return new_contact_id
        
#         else:
#             raise Exception("error:  i cen't connection! the connection is Nune")
            
#     except:
#         return False
    
#     finally:
#         if connection:
#             connection.close()




# def update_existing_contact(id, first_name, last_name, phone_number) -> (bool | None):
#     connection = get_db_connection()
#     try:
#         if connection:
#             corsor = connection.cursor()
#             query ='''
#                     UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s
#                     WHERE id = %s
#             ''' 
#             valus=(first_name, last_name, phone_number, id)

#             corsor.execute(query,valus)
#             connection.commit()
#             connection.close()
#             return True
#     except:
#         return False

# def delet_contact(id) -> bool|None:
#     connection = get_db_connection()
#     try:
#         if connection:
#             corsor = connection.cursor()
#             query ='''
#                     delete FROM contacts
#                     WHERE id = %s
#             '''
#             valus=(id,)

#             corsor.execute(query,valus)
#             connection.commit()
#             connection.close()
#             return True
#     except:
#         return False




