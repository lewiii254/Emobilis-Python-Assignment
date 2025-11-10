# Login Simulation
stored_email = "user@example.com"
stored_password = "12345"

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == stored_email and password == stored_password:
    print("Login successful!")
else:
    print("Invalid credentials!")
