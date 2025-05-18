# 📚 Calculator - Test Report

## 🧮 **Simple Calculator - First Version Review**
This report tracks the initial testing results of my Python Calculator.

### 📋 **What This Version Does**

This version:
- Asks the user to choose one of four operations.
- Requests two numbers.
- Performs the selected operation and prints the result.
- Exits after showing the result.

### 🔧 Current Code #1
```python
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
```

---

| **Test Type**        | **Main Question It Answers**                                            | **What It Focuses On**                                 |
| -------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------ |
| **Functional Tests** | *“Does the code **do the right job** when the user follows the rules?”* | **Correct results**, **correct logic**                 |
| **Input Validation** | *“Can the code **handle bad, wrong, or risky inputs** safely?”*         | **Safety**, **error handling**, **no crashes**         |
| **User Experience**  | *“Is the program **pleasant, understandable, and clear** to use?”*      | **Friendly text**, **clear flow**, **polite behavior** |

---
### 🔨 Calculator - Combined Test Report

| **Test Case** | **Test Type**         | **Input Example**            | **Expected Behavior**                                   | **Actual Behavior**               | **Status** | **Notes** |
|--------------|-----------------------|------------------------------|---------------------------------------------------------|-----------------------------------|-----------|----------|
| **TC-001**   | Functional             | `1`, `5`, `6`                 | Displays `The sum is: 11`                                | Works as expected                 | ✅ Pass    |          |
| **TC-002**   | Functional             | `2`, `5`, `3`                 | Displays `The residual is: 2`                            | Works as expected                 | ✅ Pass    |          |
| **TC-003**   | Functional             | `3`, `3`, `3`                 | Displays `The product is: 9`                             | Works as expected                 | ✅ Pass    |          |
| **TC-004**   | Functional             | `4`, `8`, `2`                 | Displays `The quotient is: 4.0`                          | Works as expected                 | ✅ Pass    |          |
|              |                       |                              |                                                         |                                   |           |          |
| **IV-001**   | Input Validation       | Invalid menu choice (e.g., 99) | Politely offers retry or exit                           | Ends with "Error. Try again" but no retry | ❌ Fail    | Needs retry loop |
| **IV-002**   | Input Validation       | Invalid number (e.g., `abc`)  | Politely offers retry or exit                           | Program crashes with ValueError   | ❌ Fail    | Needs input validation and retry |
| **IV-003**   | Input Validation       | `4`, `10`, `0`                | Displays `Cannot divide by zero!`                        | Crashes with ZeroDivisionError    | ❌ Fail    | Needs zero check  |
|              |                       |                              |                                                         |                                   |           |          |
| **UX-001**   | User Experience        | Program start                | Greets user and clearly shows menu options               | Menu shown, looks fine            | ✅ Pass    | -        |
| **UX-002**   | User Experience        | Displayed menu               | Menu is clear and readable                              | Menu is clear                     | ✅ Pass    | -        |
| **UX-003**   | User Experience        | After completing calculation  | Asks if user wants to continue or exit                   | Program ends without asking       | ❌ Fail    | Add repeat prompt |
| **UX-004**   | User Experience        | Enters `YES` or `yes` to exit | Program accepts both uppercase and lowercase input      | Not implemented                   | ⚠️ To Do   | Add .lower() normalization |
|              |                       |                              |                                                         |                                   |           |          |

---

### 🚧 What Can Be Improved in This Version

1. **Input Validation**:
    - Catch non-numeric inputs like `abc`.
    - Validate menu selection (1-4).
2. **Error Handling**:
    - Handle **division by zero** gracefully.
3. **User Experience Improvements**:
    - Offer to **repeat or exit** after each operation.
    - Accept **uppercase and lowercase** responses (`YES`, `yes`, `y`, etc.).
4. **Looping**:
    - Allow **multiple calculations** without restarting the program.
5. **Code Cleanliness (Optional Advanced Refactor)**:
    - Use **functions** to avoid repeating the same input code.
    - Add **clear error messages**.

---
