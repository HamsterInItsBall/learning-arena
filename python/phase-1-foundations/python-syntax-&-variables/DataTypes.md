# **Understanding Python Data Types**
In Python, data types define the kind of value a variable holds and determine what operations can be performed on it. 
Since Python is dynamically typed, the data type of a variable is determined at runtime based on the assigned value

---

## **What Are Data Types?**
A **data type** tells Python **what kind of data you are working with** and **what you are allowed to do with it**.

For example:
- If something is a **number**, you can **add, subtract, multiply**.
- If something is **text**, you can **join, split, or count characters**.
- If something is a **collection**, you can **loop through its elements**.


Example:
```python
  x = int(input("Enter a number: "))
```

Without data types, Python wouldn’t know whether `"2"` is a number, a string, or something else.

That’s why **data types are important**.
---

## **Python’s Main Built-In Data Types**
1. Numeric Types

Python supports three numeric types:
- int: Whole numbers like `5`, `-10`, or `1000000`
- float: Decimal numbers like `3.14`, `-1.5`, or `2.0`
- complex: Numbers with a real and imaginary part like `2 + 3j`

#### Integer Example (int):
- Whole numbers, positive or negative
- No decimal point
- You can use underscores to make big numbers easier to read

```python
  large_number = 1_000_000
  print(large_number)  # Outputs: 1000000
```
#### Floating-Point Numbers (float) Example:
- Decimal numbers
- Can use scientific notation (`1e6` means 1 million)

```python
  x = 10e100   # Scientific notation (10 to the power of 100)
  print(x)     # Outputs: 1e+100

  x = 10e400
  print(x)     # Outputs: inf (infinity, because it's too big to store)
```
#### Complex Numbers (complex) Example:
- Used in advanced math or physics
- Written as real + imaginary (`j` is the imaginary part)
  
```python
a = 10 + 3j
print(a)  # Outputs: (10+3j)
```
---
## **2. Sequence Types**
Sequences are **ordered collections**.
- String `(str)`: Text data
- List `(list)`: Changeable collections
- Tuple `(tuple)`: Unchangeable collections

#### String (str)Example:
- Text data
- Use quotes, either single or double
```python
  x = "Hello, World"
  print(x)
```
You can access characters using indexing:
```python
  word = "Python"
  print(word[0])  # Outputs: P
```

#### List (list) Example:
- Ordered, changeable, indexed
- Can store mixed types
```python
  my_list = ["apple", 42, True]
  print(my_list[0])  # Outputs: apple
```
You can **change** list items:
```python
  my_list[0] = "banana"
  print(my_list)  # ['banana', 42, True]
```

#### Tuple Example:
- Ordered, unchangeable, indexed
```python
  my_list[0] = "banana"
  print(my_list)  # ['banana', 42, True]
```
You **cannot change** tuple values after they’re created.

---

## **3. Set Types**
Sets are unordered collections with no duplicates.

#### Set Example:
```python
  x = {1, 2, 3, 4, 5, "Python"}
  print(x)  # Outputs the set without guaranteed order
```

#### Set Union Example:
```python
  x = {"Hello"}
  y = {"Python"}
  print(x | y)  # Outputs: {'Hello', 'Python'}
```
---
## **4. Mapping Type - Dictionary**
Dictionaries store key-value pairs.

```python
  my_dict = {
      "name": "John Doe",
      "client": "Python",
      "subject": "Python"
  }
  print(my_dict)
  print(my_dict["client"])  # Outputs: Python
```
Dictionaries are **super useful** for **storing structured data**.
---
## **5. Boolean Type**
Booleans represent True or False.

#### Boolean Example:
```python
  print(10 > 5)  # True
  print(5 > 10)  # False
```
Booleans are often used in **conditions** and **control flow**.
---
## **6. Range Type (range)**
- Represents a sequence of numbers
- Used mostly in loops
```python
  for i in range(3):
      print(i)  # Outputs: 0, 1, 2
```
---
## **7. Binary Types**
- **bytes, bytearray, memoryview**
- Useful for **low-level data processing**, like network communication or file reading
#### Example with bytes:
```python
  data = b"Hello"
  print(data)  # Outputs: b'Hello' 
```
---
## **8. None Type**
- **None** means "nothing" or "no value"
```python
  x = None
  print(x)  # Outputs: None
```
Commonly used to **reset variables** or represent **optional values**.
---
## **Summary Table of Data Types**
| **Category**  | **Type**                           | **Example**                    |
| ------------- | ---------------------------------- | ------------------------------ |
| **Text Type** | `str`                              | `"Hello World"`                |
| **Numeric**   | `int`, `float`, `complex`          | `20`, `20.5`, `1j`             |
| **Sequence**  | `list`, `tuple`, `range`           | `[1, 2]`, `(1, 2)`, `range(5)` |
| **Mapping**   | `dict`                             | `{"key": "value"}`             |
| **Set**       | `set`, `frozenset`                 | `{1, 2}`, `frozenset({1, 2})`  |
| **Boolean**   | `bool`                             | `True`, `False`                |
| **Binary**    | `bytes`, `bytearray`, `memoryview` | `b"Hello"`, `bytearray(5)`     |
| **None Type** | `NoneType`                         | `None`                         |
---
## **Checking the Data Type**
Use the `type()` function to check what type a variable is:

```python
  x = 5
  print(type(x))  # Outputs: <class 'int'>
```
---

## **Setting the Data Type by Assignment**
In Python, the data type is set when you assign a value:

x = "Hello"                   # str
x = 20                        # int
x = 20.5                      # float
x = 1j                        # complex
x = ["apple", "banana"]       # list
x = ("apple", "banana")       # tuple
x = range(6)                  # range
x = {"name": "John", "age": 30}  # dict
x = {"apple", "banana"}       # set
x = frozenset({"apple"})      # frozenset
x = True                      # bool
x = b"Hello"                  # bytes
x = bytearray(5)              # bytearray
x = memoryview(bytes(5))      # memoryview
x = None                      # NoneType

---

## **Why Data Types Matter**
1. **Correct Behavior**
- Knowing the type helps avoid bugs when combining, looping, or calculating.
2. **Type-Specific Operations**
- You can’t add a string and a number without converting one of them.
3. **Cleaner, Safer Code**
- Prevents type errors and unexpected results.

---
# **Python Data Type Conversion Functions**

Python provides several **built-in functions** to **convert values from one data type to another**.  
These functions return **new objects** representing the converted values.

---

## **Data Type Conversion Functions**

| **Function**       | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| `int(x, base)`     | Converts `x` to an **integer**. If `x` is a string, `base` specifies its numeric base. |
| `long(x, base)`    | Converts `x` to a **long integer** (Deprecated in Python 3).                     |
| `float(x)`         | Converts `x` to a **floating-point number**.                                    |
| `complex(x, y)`    | Creates a **complex number**.                                                    |
| `str(x)`           | Converts `x` to a **string**.                                                    |
| `repr(x)`          | Converts `x` to an **expression string** (mostly for debugging).                 |
| `eval(str)`        | **Evaluates** a **string** and returns the result as an **object**.               |
| `tuple(s)`         | Converts `s` (a sequence) to a **tuple**.                                        |
| `list(s)`          | Converts `s` (a sequence) to a **list**.                                         |
| `set(s)`           | Converts `s` (a sequence) to a **set** (no duplicates, unordered).               |
| `dict(d)`          | Creates a **dictionary** from a sequence of **(key, value)** tuples.             |
| `frozenset(s)`     | Converts `s` to a **frozen set** (immutable set).                                |
| `chr(i)`           | Converts an **integer `i`** to a **Unicode character**.                          |
| `ord(c)`           | Converts a **single character `c`** to its **integer Unicode value**.            |
| `hex(i)`           | Converts an **integer `i`** to a **hexadecimal string**.                         |
| `oct(i)`           | Converts an **integer `i`** to an **octal string**.                              |

---

## **Notes**

- ⚠️ **`long()`** and **`unichr()`** are **deprecated** in Python 3. Use **`int()`** and **`chr()`** instead.
- ⚠️ **`eval()`** is **powerful but risky**. It runs any Python expression in the string you provide.  
  Use **with caution**, especially with user input.

---

# **Primitive and Non-Primitive Data Types**

After learning about Python's different data types, I discovered that they can be **grouped into two categories**:
- **Primitive Types**  
- **Non-Primitive Types**

This helps **organize my understanding** and makes it easier to think about **how simple or complex** the data I’m working with really is.

---

## **Primitive Data Types**

Primitive data types are the **basic building blocks** in Python.  
They hold **single pieces of data** and are used to **build more complex types**.

### **The Four Primitive Types in Python:**

1. **Integers (`int`)**
   - Whole numbers like `5`, `-3`, or `1000`
   - Example:
     ```python
     age = 25
     print(age)
     ```

2. **Floats (`float`)**
   - Decimal numbers like `3.14`, `-0.5`, or `2.0`
   - Example:
     ```python
     price = 19.99
     print(price)
     ```

3. **Booleans (`bool`)**
   - **True** or **False**
   - Example:
     ```python
     is_active = True
     print(is_active)
     ```

4. **Strings (`str`)**
   - Sequences of **text characters**, like `"Hello"` or `'Python'`
   - Example:
     ```python
     name = "Alice"
     print(name)
     ```

---

## **Non-Primitive (or Complex) Data Types**

Non-primitive data types are **collections or structures** that can store **multiple values** or **key-value pairs**.  
These types **group data together** and are often used to build **larger, more complex programs**.

### **The Four Common Non-Primitive Types in Python:**

1. **Lists (`list`)**
   - **Ordered**, **changeable** collections  
   - Example:
     ```python
     fruits = ["apple", "banana", "cherry"]
     print(fruits)
     ```

2. **Tuples (`tuple`)**
   - **Ordered**, **unchangeable** collections  
   - Example:
     ```python
     coordinates = (10, 20)
     print(coordinates)
     ```

3. **Dictionaries (`dict`)**
   - **Unordered**, **key-value pairs**  
   - Example:
     ```python
     person = {"name": "Alice", "age": 30}
     print(person)
     ```

4. **Sets (`set`)**
   - **Unordered**, **unique values**, **no duplicates**
   - Example:
     ```python
     unique_numbers = {1, 2, 3, 3}
     print(unique_numbers)  # Outputs: {1, 2, 3}
     ```

---

## **Why This Categorization Matters**

Understanding the difference between **primitive** and **non-primitive** data types helps me:
- **Choose the right type** based on the problem I’m solving.
- **Understand memory usage** (primitive types are lighter, non-primitive can hold more data).
- **Design better data structures** for future projects.

For example:
- If I need to store **a single user name**, I’ll use a **string** (primitive).
- If I need to store **a list of users**, I’ll use a **list** or **dictionary** (non-primitive).

---
