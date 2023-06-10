#plik '.env musi być dostępny zaraz na początku, bo z niego się pobiera hasło do konta. Nie może ten plik .env być w jakimś katalogu  schowany,
# bo kod już w innym katalogu wtedy nie zadziała

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

# connection.execute("Create Table users(id int identity, name varchar(100), age int)") #tu jak stworzę tabele w pliku 2 to muszę tą linię dezaktywaować
connection.execute("INSERT INTO users(name, age) VALUES ('Andrzej', 29)")
connection.execute("INSERT INTO users(name, age) VALUES ('Maciej', 35)")
connection.execute("INSERT INTO users(name, age) VALUES ('Maciej', 35)")
connection.execute("INSERT INTO users(name, age) VALUES ('Maciej', 35)")
connection.execute("INSERT INTO users(name, age) VALUES ('Maciej', 35)")
connection.execute("INSERT INTO users(name, age) VALUES ('Maciej', 35)")
connection.execute("INSERT INTO users(name, age) VALUES ('Maciej', 35)")
connection.execute("INSERT INTO users(name, age) VALUES ('Maciej', 35)")
connection.execute("INSERT INTO users(name, age) VALUES ('Maciej', 35)")



cursor = connection.cursor()

cursor.execute("SELECT * From users")
result = cursor.fetchmany(5)

# for id, name , age in cursor:
#     print(id)
#     print(name)
#     print(age)
#     print(20 * '-')


cursor.execute("SELECT * From users")
# results = cursor.fetchall()
result = cursor.fetchone()
# print(results)

while result:
    print(result)
    result = cursor.fetchone()

# for row in cursor:
#     print(row)



# for id, name , age in cursor:
#     print(id)
#     print(name)
#     print(age)
#     print(20 * '-')



cursor.close()
connection.close()


