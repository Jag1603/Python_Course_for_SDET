class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        if amount <= 0: raise ValueError("Amount must be positive")
        self._balance += amount
account = BankAccount(100)
account.deposit(50)
print(account.balance)