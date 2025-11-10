# Login Attempts
password = "pass123"
attempts = 0

while attempts < 3:
    entry = input("Enter password: ")
    if entry == password:
        print("Access granted")
        break
    else:
        print("Wrong password, try again")
        attempts += 1
else:
    print("Account locked.")