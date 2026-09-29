class Discount:
    def apply(self, amount): raise NotImplementedError
class VipDiscount(Discount):
    def apply(self, amount): return amount * 0.8
print(VipDiscount().apply(100))