users = [{"name":"A","age":30},{"name":"B","age":20}]
print(sorted(users, key=lambda u: u["age"]))