class InsufficientBalanceError(Exception): pass

def withdraw(balance, amount):
    if amount > balance: raise InsufficientBalanceError("Insufficient balance")
    return balance - amount
try: withdraw(50,100)
except InsufficientBalanceError as e: print(e)