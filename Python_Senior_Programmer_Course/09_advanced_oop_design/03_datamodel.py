class Box:
    def __init__(self, items): self.items = items
    def __len__(self): return len(self.items)
    def __contains__(self, item): return item in self.items
b=Box([1,2,3]); print(len(b), 2 in b)