def user_data(**overrides):
    data={"name":"Test User","role":"user"}
    data.update(overrides)
    return data
print(user_data(role="admin"))