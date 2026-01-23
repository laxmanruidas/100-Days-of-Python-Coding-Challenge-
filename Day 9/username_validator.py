# Day 9 
# 100 Days of Python Challenge

while True:
    print("Username Validator")
    print("--------------------------")

    username = input("Enter username: ").strip()

# minimum length check
    if len(username) < 5:
        print("username must be at least 5 characters long")

    # no spaces allowed
    elif " " in username:
        print("username should not contain spaces")

    # only letters and numbers
    elif not username.isalnum():
        print("Username can contain only letters and numbers")

    else:
        print("Username is valid!")
        print(f"Welcome, {username}")

    choice = input("Do you want to check another username? (y/n): ").lower().strip()
    if choice != "y":
        print("Program End!")
        break
