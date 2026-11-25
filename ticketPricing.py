age = int(input("Please enter your age: "))
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2

print(f"The ticket price is: ${price}")
