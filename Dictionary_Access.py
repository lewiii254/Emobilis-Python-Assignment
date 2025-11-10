# Dictionary Access Validation
user_profile = {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "verified": False
}

verify = input("Has the user verified their account? (yes/no): ").lower()

if verify == "yes":
    user_profile["verified"] = True
    print("Updated profile:", user_profile)
else:
    print("Verification pending.")
