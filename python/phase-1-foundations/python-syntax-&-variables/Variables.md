# **Learning About Variables in Python**

Today I started digging deeper into **variables**.  
I’ve already used a few, like when I stored my name in the `input()` example earlier.  
But I realized I don’t really understand **what’s going on under the hood**,  
so I decided to take proper notes to make sure I *actually* understand variables in Python.

---

## **What Is a Variable?**

A **variable** is like giving something a **name** so you can refer to it later.  
It’s a **label** that holds **data**.

For example, when I write:

#### Example:
  ```python
  x = 5
  y = "Leo"
  print(x)
  print(y)
  ```
I’m saying: 
- x holds the number 5
- y holds the text "Leo"
  
Python remembers this, so when I later say:
  ```python
  print(x)
  print(y)
  ```
It knows to print 5 and John.

---

##**Creating Variables**

Python is very loose about creating variables compared to some other languages like Java or C++.

In Python:
- I don’t need to tell it "Hey, this is going to be a number" or "This is going to be text."
- Python **figures it out on its own** when I assign the value.
  
#### Example:
  ```python
  x = 4          # Python sees this as a number (int)
  x = "Techo"    # Now x holds a string (str), and that's totally fine in Python
  ```
It **changes the type** based on what I assign. This is called **dynamic typing**.

---
## **Forcing a Specific Type (Casting)**

Sometimes I might want to be specific about the type, especially when converting **between types**.
 ```python
  x = str(3)    # Now x holds '3' as a string
  y = int(3)    # y holds the number 3 as an integer
  z = float(3)  # z holds 3.0 as a float (decimal)
 ```
---

## **Checking the Type of a Variable**
I can check what type a variable has by using `type()`:
 ```python
   x = 5
   y = "Blade"
   print(type(x))  # <class 'int'>
   print(type(y))  # <class 'str'>
  ```
--- 
## **Single vs Double Quotes**

Both work **exactly the same** for text (strings):
 ```python
  x = "Frog"
  y = 'Frog'
 ```
If I have quotes inside my text, I can **mix them**:
 ```python
  quote = "It's a beautiful day"
  quote = 'He said, "Hello!"'
 ```

---

## **Case Sensitivity**
Python **treats uppercase and lowercase letters differently**.
 ```python
  a = 4
  A = "Sally"
 ```
- a and A are different variables.

---

## **Why Good Variable Names Matter**
It’s tempting to name everything `x`, `y`, or `var1`, but that makes the code **hard to read later**.
Good names explain what the variable holds, like:
 ```python
  username = "Maria"
  age = 27
 ```
This makes it easier for **me** and **others** to understand the code later, even after I forget what I wrote.


## **Variable Naming Rules**
Python is picky about naming:
- Must start with a letter or underscore
- Can’t start with a number
- Only letters, numbers, and underscores are allowed
- No spaces, hyphens, or special symbols
- Case-sensitive (e.g., `myVar`, `MyVar`, and `MYVAR` are different)

#### Examples of legal names:
 ```python
  myvar = "John"
  my_var = "John"
  _my_var = "John"
  myVar = "John"
  MYVAR = "John"
  myvar2 = "John"
 ```
#### Examples of illegal names:
 ```python
2myvar = "John"   # Cannot start with a number
my-var = "John"   # Cannot contain hyphens
my var = "John"   # Cannot contain spaces
  ```
---

## **Naming Styles for Multi-Word Variables**
Python style guides (PEP8) recommend **snake_case**,
but I’ve also seen these other styles:
- Camel Case: myVariableName
- Pascal Case: MyVariableName
- Snake Case: my_variable_name <- Python’s preferred style
  
---
---

## **Assigning Multiple Variables at Once**
 ```python
  x, y, z = "Orange", "Banana", "Cherry"
  print(x)
  print(y)
  print(z)
  ```
Make sure the **number of variables matches the number of values**.

---

## **Assigning the Same Value to Multiple Variables**
 ```python
  x = y = z = "Orange"
  print(x, y, z)
  ```

---

## **Unpacking Collections Into Variables**
  ```python
  fruits = ["grape", "mango", "cherry"]
  x, y, z = fruits
  print(x)
  print(y)
  print(z)
  ```
---

## **Printing Variables**
### **Single Variable:**
  ```python
 x = "Python is awesome"
 print(x)
  ```

### **Multiple Variables with Commas:**
  ```python
  x = "Python"
  y = "is"
  z = "awesome"
  print(x, y, z)
  ```

### **Concatenating Strings with +:**
  ```python
  print(x + y + z)
  ```
### **⚠️ Mixing numbers and strings requires care:**
  ```python
  x = 5
  y = "John"

  print(x, y)       # This works
  # print(x + y)    # This throws an error
  ```
---

## **Practice: Adding Two Numbers From User Input**
I tried building a small script to ask for two numbers and add them:
  ```python
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  print("The sum is:", num1 + num2)
  ```
This helped me practice:
- Storing user input
- Converting text to numbers with `int()`
- Printing the result
  
---
## **Global vs Local Variables**
### **Global Variables (Available Everywhere)**
A **global variable** is **created outside** of any function.
This means it can be **used anywhere** in the file — inside or outside functions.

#### Global Example:
  ```python
  x = "awesome" # Global variable

  def myfunc():
    print("Python is " + x) # Uses the global variable

  myfunc()
  ```
- x is defined outside the function.
- -The function can access it without any problems.
So **global variables** are **"shared"** across the whole file.

### **Local Variables (Available Only Inside the Function)**
A **local variable** is **created inside** a function.
It **only exists while the function runs**, and **only inside** that function.

#### Local Example:
  ```python
  x = "awesome" # Global variable

  def myfunc():
      x = "fantastic" # Local variable, only exists inside myfunc
      print("Python is " + x)

  myfunc()
  print("Python is " + x) # This prints "awesome", not "fantastic"
  ```
- Inside `myfunc()`, `x` is **"fantastic"** (this is a **local** version of `x`).
- Outside `myfunc()`, `x` is still **"awesome"** (the **global** one didn’t change).
This means the **function creates its own copy** and **does not touch the global variable**.

## Why This Matters
- Local variables protect your code from accidentally changing important values.
- But if you want to change the global variable, you have to declare it using the global keyword.

#### Example of Changing a Global Variable:
  ```python
  x = "awesome"

  def myfunc():
      global x  # Tells Python to use the global variable
      x = "fantastic"

  myfunc()
  print("Python is " + x)  # Now x has changed to "fantastic"
  ```

---
## **Using global to Modify Global Variables**
  ```python
  x = "awesome"

  def myfunc():
      global x
      x = "fantastic"

  myfunc()
  print("Python is " + x)
  ```
---

## **Be Careful Not to Overwrite Built-In Names**
Python has built-in functions like `list()`, `str()`, `input()`, and `print()`.
Accidentally **using these as variable names can break other parts of my code**.

Example of what **not** to do:
  ```python
  list = [1, 2, 3]  # This blocks the built-in list() function
  ```
It’s better to use names like:
  ```python
  my_list = [1, 2, 3]
  ```
---

## **Reassigning Variables to Different Types**
Python lets me **change the type** of a variable anytime,
but this can **lead to confusing bugs** if I’m not careful.
  ```python
  age = 22        # age is a number
  age = "twenty two"  # age is now a string
  ```
It’s usually better to **keep the meaning** of a variable consistent.
---

## **(Advanced Curiosity) Variables Are References, Not Boxes**
In Python, variables don’t actually "hold" the data.
They *point* to data in **memory**.
#### For example:
  ```python
  a = [1, 2, 3]
  b = a  # b points to the same list as a
  b.append(4)
  print(a)  # [1, 2, 3, 4] — a changed too!
  ```
Both `a` and `b` **share the same memory reference**.
This is called **referencing**, and it’s something I might explore more deeply later.

