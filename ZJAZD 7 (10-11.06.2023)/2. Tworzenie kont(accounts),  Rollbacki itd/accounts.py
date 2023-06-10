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
            print(f"{amount} withraw from account {self.name}")

    def show_balance(self):
        print(f"Account {self.name} balance: {self._balance}")


if __name__ == '__main__':
    account = Account('Andrzej')
    account.deposit(10)
    account.deposit(0.1)
    account.deposit(0.3)
    account.deposit(7.2)
    account.show_balance()
    # as
