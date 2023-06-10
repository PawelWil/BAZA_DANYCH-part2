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

#----------------to powyżej to connection ustawienia ODBC








class Account:

    def __init__(self, name: str, open_balance: float = 0.0):
        self.name = name
        self._balance = open_balance
        print(f"Account {name} created with opening balance {round(open_balance, 2)}")

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited to Account {self.name}")

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdraw from account {self.name}")

    def show_balance(self):
        print(f"Account {self.name} balance: {self._balance}")


if __name__ == '__main__':
    account = Account('Andrzej')
    account.deposit(10)
    account.deposit(0.1)
    account.deposit(0.3)
    account.deposit(7.2)
    account.show_balance()

