# first_script.py

# This line prints a simple greeting message to the screen
print("Hello, World!")

# This line asks the user to enter their name and stores the response in the variable 'user_name'
user_name = input("What is your name? ")

# This line prints a personalized message using the value the user provided
# The f"" syntax is called an 'f-string', which allows you to embed variables directly inside a string
print(f"Nice to meet you, {user_name}! Welcome to Python learning.")

# The '\n' creates a line break (a blank line) for better readability in the terminal
# This line then waits for the user to press Enter before the program closes
input("\nPress Enter to exit the program...")
