def add_item(items=[]):
    items.append(1)
    return items
print(add_item())
print(add_item())
print("Avoid mutable default arguments; use None.")