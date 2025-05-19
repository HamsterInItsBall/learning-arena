print("Welcome to the Calculator!")
print("Choose available operations:\n")
print("1. Add number to number")
print("2. Subtract number from number")
print("3. Multiplication of two numbers")
print("4. Division of two numbers\n")

user_choice = int(input("What operations you want made: "))
if user_choice == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The sum is:", num1 + num2)
elif user_choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The residual is:", num1 - num2)
elif user_choice == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The product is:", num1 * num2)
elif user_choice == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The quotient is:", num1 / num2)
else: 
    print("Error. Try again")

input("\nPress Enter to exit the program...")
