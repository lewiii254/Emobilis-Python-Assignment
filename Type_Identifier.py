# Type Identifier
value = input("Enter any value: ")

print("Raw input:", value)

if value.isdigit():
    print("Data type: int")
elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
    print("Data type: float")
else:
    print("Data type: str")
