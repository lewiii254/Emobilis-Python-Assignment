# Collection Sorter
numbers = [4, 15, 9, 23, 7, 18, 3]
count = 0

for num in numbers:
    if num <= 10:
        continue
    print(num)
    count += 1

print(f"Total numbers greater than 10: {count}")
