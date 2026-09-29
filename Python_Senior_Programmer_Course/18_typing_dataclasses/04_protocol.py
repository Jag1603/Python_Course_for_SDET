from typing import Protocol
class HasName(Protocol):
    name: str
class User:
    def __init__(self,name): self.name=name
def print_name(obj: HasName): print(obj.name)
print_name(User("Ada"))