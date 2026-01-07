# what is my project today '
# Day 2 - Simple Calculator
# This is my Day 2 project of 100 Days of Python Challenge
# I am learning user input and if-else condition

print("Welcome to Simple Calculator")

# Take first number from user
num1 = int(input("Enter first number: "))

# Take second number from user
num2 = int(input("Enter second number: "))

print("\nChoose an operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Take user choice
choice = input("Enter your choice (1/2/3/4): ")

# Check choice and calculate
if choice == "1":
    result = num1 + num2
    print("Result:", result)

elif choice == "2":
    result = num1 - num2
    print("Result:", result)

elif choice == "3":
    result = num1 * num2
    print("Result:", result)

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid choice")
print("Created by Laxman")
print("Code end !")
