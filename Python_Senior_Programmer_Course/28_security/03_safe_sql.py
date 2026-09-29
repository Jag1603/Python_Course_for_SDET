# Always parameterize SQL instead of concatenating user input.
query = "SELECT * FROM users WHERE name = ?"
params = ("Ada",)
print(query, params)