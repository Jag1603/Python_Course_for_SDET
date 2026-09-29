class TaxStrategy:
    def calculate(self, amount): raise NotImplementedError
class IndiaTax(TaxStrategy):
    def calculate(self, amount): return amount * 0.18
class Checkout:
    def __init__(self, strategy): self.strategy=strategy
    def total(self, amount): return amount + self.strategy.calculate(amount)
print(Checkout(IndiaTax()).total(100))