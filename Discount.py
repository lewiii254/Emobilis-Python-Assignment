# Discount Program
product = input("Enter the product name: ")
price = float(input("Enter the product price: "))

if price > 10000:
    discount = 0.20
elif 5000 <= price <= 10000:
    discount = 0.10
else:
    discount = 0.0

discounted_price = price * (1 - discount)
print(f"The {product} now costs {discounted_price:.2f} after discount.")
