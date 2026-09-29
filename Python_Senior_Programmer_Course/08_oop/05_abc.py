from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount): pass
class CardPayment(Payment):
    def pay(self, amount): return f"Paid {amount} by card"
print(CardPayment().pay(100))