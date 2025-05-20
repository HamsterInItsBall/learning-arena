Now it's look like this:
print("Welcome to the Calculator!")
print("Choose available operations:\n")
print("1. Add number to number")
print("2. Subtract number from number")
print("3. Multiplication of two numbers")
print("4. Division of two numbers\n")

def get_two_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error. Please enter valid numbers.")
        return None,None

def main():
    try:
        user_choice = int(input("What operations you want made: "))
    except ValueError:
        print("Error. Please enter a number (1, 2, 3, or 4).")
        return
    
    if user_choice == 1:
        num1, num2 = get_two_numbers()
        if num1 is None:
            return  # Go back to start
        print("The sum is:", num1 + num2)
    elif user_choice == 2:
        num1, num2 = get_two_numbers()
        if num1 is None:
            return  # Go back to start
        print("The residual is:", num1 - num2)
    elif user_choice == 3:
        num1, num2 = get_two_numbers()
        if num1 is None:
            return  # Go back to start
        print("The product is:", num1 * num2)
    elif user_choice == 4:
        num1, num2 = get_two_numbers()
        if num1 is None:
            return  # Go back to start
        print("The quotient is:", num1 / num2)
    else: 
        print("Error. Try again")

while True:
    main()

    user_choice2=input("Would you like to exit?: ").lower()
    if user_choice2=='y' or user_choice2=='ye' or user_choice2=='yes' :
        break
    elif user_choice2=='n' or user_choice2=='no':
        pass
