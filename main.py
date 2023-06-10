import os

import pyodbc
from dotenv import load_dotenv

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD') # 1 sposób importu hasla
database_server = 'morfeusz.wszib.edu.pl'
database_name = 'wiltos'
database_user = 'wiltos'
driver = '{ODBC Driver 18 for SQL Server}'
# password_two = os.environ.get("PASSWORD_TWO") # 2 sposób importu hasla

# print(database_password) # 1 sposób importu hasla
# print(password_two) # 2 sposób importu hasla

connection_string = f'Driver={driver};' \
                    f'SERVER={database_server};'\
                    f'DATABASE={database_name};'\
                    f'UID={database_user};' \
                    f'PWD={database_password};' \
                    'Encrypt=no;'


connection = pyodbc.connect(connection_string)

connection.execute("Create Table users(id int identity, name varchar(100), age int)")
connection.execute("INSERT INTO users(name, age) VALUES ('Andrzej', 29)")
connection.execute("INSERT INTO users(name, age) VALUES ('Maciej', 35)")


cursor = connection.cursor()


cursor.execute("SELECT * From users")
for id, name , age in cursor:
    print(id)
    print(name)
    print(age)
    print(20 * '-')


cursor.execute("SELECT * From users")
for id, name , age in cursor:
    print(id)
    print(name)
    print(age)
    print(20 * '-')

    
cursor.close()
connection.close()


