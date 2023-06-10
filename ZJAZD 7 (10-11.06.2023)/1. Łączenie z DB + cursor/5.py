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
cursor = connection.cursor()

update_sql = []


new_name = input('Proszę podać imię: ')


sql = f"UPDATE users SET email = 'update@sql.injection' WHERE name = {new_name}"

split_arr = sql.split(';')

for update in split_arr:
    cursor.execute(update)

cursor.commit()

cursor.close()
connection.close()


