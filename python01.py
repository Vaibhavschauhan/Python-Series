userage = int(input("Please enter your age: "))
if userage < 13:
    print("You are a minor.")
elif userage <= 18:
    print("You are a teenager.")
elif userage <= 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")