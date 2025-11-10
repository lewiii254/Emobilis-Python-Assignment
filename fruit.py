# Favorite Fruits (Nested Loop Challenge)
colors = ["red", "green", "yellow"]
fruits = ["apple", "banana", "pear"]

total_combinations = 0

# 1. Write a nested for loop
print("--- Color-Fruit Combinations ---")
for color in colors:
    for fruit in fruits:
        # Print the combination
        print(f"{color} : {fruit}")
        total_combinations += 1

# 2. Print the total number of combinations printed
print(f"Total number of combinations printed: {total_combinations}")