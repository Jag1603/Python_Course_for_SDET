try:
    value = int("abc")
except ValueError as exc:
    print("Invalid number:", exc)
else:
    print(value)
finally:
    print("Finished")