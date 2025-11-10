# Nested Data Lookup
myFamily = {
    "father": {"name": "John", "year": 1985},
    "mother": {"name": "Jane", "year": 1990}
}

person = input("Enter 'father' or 'mother': ").lower()

if person in myFamily:
    member = myFamily[person]
    print(f"Name: {member['name']}, Year of birth: {member['year']}")
else:
    print("Family member not found.")
