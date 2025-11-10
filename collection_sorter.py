# Collection Sorter
import random

# 1. Create a list of 7 random integers (e.g., between 5 and 20)
number_list = [random.randint(5, 20) for _ in range(7)]
print(f"Original list: {number_list}")

count_greater_than_10 = 0

# 2. Use a loop
print("--- Processing Numbers ---")
for num in number_list:
    if num <= 10:
        # Skip (using continue) numbers less than or equal to 10
        continue
    
    # This code only runs if num > 10
    print(f"Number greater than 10: {num}")
    count_greater_than_10 += 1

# 3. Print the total count
print(f"--- Results ---")
print(f"Total number of values greater than 10: {count_greater_than_10}")