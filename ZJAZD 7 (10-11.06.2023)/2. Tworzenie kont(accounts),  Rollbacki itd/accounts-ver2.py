#plik '.env musi być dostępny zaraz na początku, bo z niego się pobiera hasło do konta. Nie może ten plik .env być w jakimś katalogu  schowany,
# bo kod już w innym katalogu wtedy nie zadziała


import os

import pyodbc
from dotenv import load_dotenv
from datetime import datetime

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

#----------------to powyżej to connection ustawienia poprzez ODBC--------^


class Account:

    @staticmethod
    def current_time():
        return datetime.now()

    def __init__(self, name: str, open_balance: float = 0.0):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO accounts (account_name, account_balance) VALUES (?,?)", (name, open_balance))
            cursor.execute("SELECT @@IDENTITY AS ID")
            self.id = cursor.fetchone()[0]
            self.name = name
            self._balance = open_balance
            print(f"Account {name}, [id={self.id}] created with opening balance {round(open_balance, 2)}")

    def deposit(self, amount: float):
        if amount > 0:
            with connection.cursor() as cursor:
                self._balance += amount
                cursor.execute("UPDATE accounts SET account_balance = ? WHERE account_id = ?",
                               (self._balance, self.id))
                cursor.execute("INSERT INTO transactions (account_id, transaction_time, amount) VALUES (?,?,?)",
                               (self.id, Account.current_time(), amount))
                print(f"{amount} deposited to Account {self.name}")

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            with connection.cursor() as cursor:
                self._balance -= amount
                cursor.execute("UPDATE accounts SET account_balance = ? WHERE account_id = ?",
                               (self._balance, self.id))
                cursor.execute("INSERT INTO transactions (account_id, transaction_time, amount) VALUES (?,?,?)",
                               (self.id, Account.current_time(), -amount))
                print(f"{amount} withdraw from account {self.name}")

    def show_balance(self):
        print(f"Account {self.name} balance: {self._balance}")


def do_transaction(account_from: Account, account_to: Account, amount: float):
    account_from.withdraw(amount)
    account_to.deposit(amount)


if __name__ == '__main__':
    account = Account('Andrzej', 100)
    account_two = Account('Maciej', 50)
    do_transaction(account_two, account, 51)

    connection.close()
