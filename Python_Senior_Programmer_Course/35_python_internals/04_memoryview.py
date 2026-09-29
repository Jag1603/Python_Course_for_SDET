data=bytearray(b"hello")
view=memoryview(data)
view[0]=72
print(data)