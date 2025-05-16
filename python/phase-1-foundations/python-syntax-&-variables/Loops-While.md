# Learning Python Loops 

## Getting Started With Python `while` Loops
A `while` loop **repeats a block of code** as long as a **condition is True**. 
It is commonly used when you **don’t know in advance** how many times you’ll need to repeat the task.

### Basic Concept:
- **Checks the condition first**.
- **Executes the block** if the condition is **True**.
- **Repeats** until the condition becomes **False**.
  
### Why It Exists
- To allow conditional repetition of tasks.
- Useful for waiting on events, user input, or ongoing checks.
  
#### Syntax:
```python
  while <condition>:
      <block of code>
```

#### Example:
```python
  count = 0
  while count < 5:
      print("Count is:", count)
      count += 1
```
This prints numbers 0 to 4 because it stops when `count` reaches 5.

---

## When to Use `while` Loops
Use `while` loops when **you don't know in advance how many times** you need to repeat the task.

### Example:
- Waiting for user input.
- Repeating until a condition changes.
- Polling for updates or sensor data.
---

## `while True`: Creating Infinite Loops
`while True` creates an **infinite loop** that runs forever unless you **manually stop it** with:
- A `break` statement
- An `external interruption` (like stopping the program)

#### Example:
```python
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == 'exit':
        break
    print("You typed:", user_input) # Echo the input
```
---

## Python Has No Built-in `do-while` Loop
Python does not have a native `do-while` loop like some other languages,
but you can simulate one using `while True` and `break`.

#### Example of Simulated `do-while`:
```python
while True:
    number = int(input("Enter a number greater than 0: "))
    if number > 0:
        break # Exit only if the number is valid
print("You entered:", number)
```
---

## Using Advanced `while` Loop Syntax
1. `break`: Exiting a Loop Early
   Use `break` to **stop the loop** when you’ve reached a stopping condition.
   
#### Example:
```python
while True:
    answer = input("Continue? (y/n): ")
    if answer == 'n':
        break
    print("Still going!")
```
---
2. `continue`: Skipping an Iteration
    Use `continue` to **skip the rest of the current loop** and **start the next iteration**.
   
#### Example:
```python
count = 0
while count < 5:
    count += 1 # Increase count by 1 first
    if count == 3: # Skip printing when count is 3
        continue # Go to the next iteration
    print(count) # Print count if not skipped
```
This will **skip printing 3**, showing 1, 2, 4, 5.
---

3. `else`: Running Code at Natural Termination
Use `else` with `while` to **run code when the loop finishes naturally**, without being interrupted by `break`.
#### Example:
```python
count = 0
while count < 3:
    print("Counting", count)
    count += 1
else:
    print("Finished counting!")
```
If you add a `break`, the `else` will **not run**:
```python
count = 0
while count < 3:
    print("Counting", count)
    break # Exit the loop early
else:
    print("This won't run because of break") # Skipped because of break
```
----

## Writing Effective while Loops in Python
### 1. Running Tasks Based on a Condition With `while` Loops]
`while` loops are ideal when you need to **repeat actions until a condition changes**.

#### Example: Retry Until Successful Login
```python
password = "python"
user_input = ""

while user_input != password:
    user_input = input("Enter the password: ")

print("Access granted!")
```
**! Why use this?**
  - Repeats until the user provides the correct password.
**Tricky moment:**
  - If the initial value of `user_input` accidentally matches `password`,
    the loop will **never run**. Initialize your control variable safely.

---
### 2. Using `while` Loops for an Unknown Number of Iterations
Sometimes you don't know how many times to loop. `while` loops handle this well.

#### Example: Waiting for User to Type 'stop'
```python
while True:
    command = input("Type 'stop' to exit: ")
    if command == 'stop':
        break
    print("You typed:", command)
```
**! Why use this?**
  - Keeps asking until the user **explicitly stops** the loop.
**Tricky moment:**
  - If you forget the `break`, this loop will **never stop**. Always ensure there’s a clear exit strategy.
    
---
### 3. Removing Items From an Iterable in a Loop
Be careful when **removing items while looping** over lists. It’s best to use `while` with **pop()** or **slicing**.

#### Example: Emptying a List Safely
```python
tasks = ["task1", "task2", "task3"]

while tasks:
    current_task = tasks.pop()  # Removes the last item
    print("Processing:", current_task)
```
**! Why use this?**
  - Efficiently **processes and removes items** one by one until the list is empty.
**Tricky moment:**
  - Modifying a list while looping over it with `for` can cause errors or skip items.
  - Using `pop()` ensures safe removal **without index shifting issues**.
    
---
### 4. Getting User Input With a `while` Loop
`while` is great for **validating user input**.

#### Example: Input Validation Loop
```python
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print("Your age is", age)
        break
    else:
        print("Please enter a valid number.")
```
**! Why use this?**
  - **Repeats until valid input** is entered.
**Tricky moment:**
  - Be aware that `isdigit()` **only works for positive integers**.
    It won’t accept negative numbers or floats.

---
### 5. Traversing Iterators With `while` Loops
`while` can be used to **manually step through iterators**.

#### Example: Using `next()` With an Iterator
```python
numbers = iter([1, 2, 3])

while True:
    try:
        num = next(numbers)
        print(num)
    except StopIteration:
        break
```

**! Why use this?**
  - **Handles iterators safely**, stopping when there are no more items.
**Tricky moment:**
  - Forgetting to catch `StopIteration` will **crash your program**.
    Always wrap `next()` calls in `try/except` if the end isn’t guaranteed.
    
---
### 6. Emulating Do-While Loops
Python doesn’t have a `do-while` loop, but you can **simulate one** with `while True` and `break`.

#### Example: Run at Least Once
```python
while True:
    choice = input("Type 'yes' to continue or 'no' to stop: ")
    if choice == 'no':
        break
    print("You chose to continue.")
```
**! Why use this?**
  - Ensures the loop **runs at least once** before checking conditions.
**Tricky moment:**
  - If you forget the `break`, the loop **won’t terminate**.
  - Always pair `while True` with a **clear exit condition**.
    
---

## Using `while` Loops for Event Loops
In many applications, especially **interactive programs, GUIs,** or **games**, 
you often need a loop that keeps the program "alive" until the user or 
the system decides to stop it. These are known as event loops.

#### Example: Simple Event Loop
```python
running = True

while running:
    command = input("Enter command (type 'exit' to stop): ")
    if command == 'exit':
        running = False
    else:
        print("Command received:", command)
```

**! Why use this?**
  - Keeps a program **responsive to events or user input** until an exit condition is met.
**Tricky moment:**
  - If you **don’t check** for an exit command, the loop **runs forever**.

---
## Exploring Infinite `while` Loops

### 1. Unintentional Infinite Loops
An **unintentional infinite loop** happens when your **exit condition is never met** or is **incorrectly designed**.

#### Example: Missing Increment (Unintentional Loop)
```python
count = 0

while count < 5:
    print("Stuck here forever!")  # Missing count += 1
```

**Why this happens:**
  - The variable `count` **never changes**, so the condition **stays True forever**.

#### How to fix:
```python
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
```

**Tricky moment:**
  - Always ensure **loop conditions eventually change** to avoid freezing your program.

---

### 2. Intentional Infinite Loops
Sometimes you **want** a loop that runs **indefinitely**—until something **external** tells it to stop.

#### Example: Server or Application Waiting for Events
```python
while True:
    event = input("Waiting for event (type 'shutdown' to stop): ")
    if event == 'shutdown':
        break
    print("Handling event:", event)
```

**! Why use this?**
  - Needed for **servers, games, or GUIs** that should **stay alive** waiting for user actions.
**Tricky moment:**
  - Forgetting the `break` condition can **lock the program**.
  - Always provide a **controlled exit mechanism**.
