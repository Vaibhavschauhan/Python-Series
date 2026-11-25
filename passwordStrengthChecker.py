password = str(input("Enter your password: "))

if len(password) < 6:
    print("Weak password: Password must be at least 6 characters long.")
elif len(password) < 10:
    print("Moderate password: Consider using a longer password for better security.")
else:
    print("Strong password: Your password is strong.")
