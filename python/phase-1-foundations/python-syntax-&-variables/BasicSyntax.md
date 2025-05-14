# **Basic Syntax - How Python Code Is Structured**

After writing my first script, I started to wonder — *how does Python actually expect me to write code properly?*  
In this note, I break down Python’s structure in simple terms, using real-life examples to help me understand it better. 
I’ve also included a table of common beginner mistakes to help me avoid them as I continue learning.

---

## **1. How Python Code Is Structured**

### **Reading Python Is Like Following Step-by-Step Instructions**

Python reads code **from top to bottom**, just like following a recipe or instruction manual.  
You can't pour water into a cup *before* you boil it. Python expects your instructions to make sense in order. 

Example in plain English:
1. Open the fridge
2. Take out the milk
3. Pour the milk into a glass
4. Drink the milk

#### Python Example:
```python
print("Open the fridge")
print("Take out the milk")
print("Pour the milk into a glass")
print("Drink the milk")
```

---
### **Python Uses Indentation, Not Curly Braces**

In other languages like C++, Java, or JavaScript, you group code blocks using curly braces `{}`.
Example in JavaScript:
```javascript
if (isMorning) {
    console.log("Brush teeth");
    console.log("Make breakfast");
}
```
Python does **not** use curly braces.
Instead, Python uses **indentation** — usually **4 spaces** — to define what belongs to the same block.

#### Python Example:
```python
is_thirsty = True

if is_thirsty:
    print("Drink water")  # This line is part of the 'if' block because it is indented
```
⚠️ **Mixing spaces and tabs or using inconsistent indentation will cause errors.**

---
### **Python Doesn’t Require Semicolons**

Other languages often require semicolons `;` at the end of each line.
Python **does not require semicolons.**

#### Python Example:
```python
print("Hello")  # Correct and clean
print("World"); print("No semicolons needed")  # This works, but it's not recommended
```
---
### **Comments Are Notes For Myself (and Others)**

Python ignores any line that starts with `#`.
This is useful for leaving reminders, explanations, or documentation.

#### Python Example:
```python
# This prints a welcome message
print("Welcome to Python!")
```
I can use comments to:
- Remind myself what the code does.
- Explain why something is written a certain way.
- Help others understand my code.

---
## **2. What to Watch Out For - Beginner Mistakes Table**

Here’s a table I created to remind myself of the **most common mistakes beginners make** when writing Python code.

| **Mistake** | **What Happens** | **Correct Way** |
| --- | --- | --- |
| ❌ Mixing tabs and spaces | IndentationError | Use **4 spaces consistently**, no mixing |
| ❌ Forgetting to indent | IndentationError | Always indent blocks after `if`, `for`, `while`, etc. |
| ❌ Using `=` instead of `==` | SyntaxError or unexpected behavior | Use `=` to assign, `==` to compare |
| ❌ Adding unnecessary semicolons | Not an error, but bad style | Leave semicolons off unless writing one-liners |
| ❌ Overwriting built-in names (like `list`) | Breaks access to built-in types/functions | Use custom variable names like `my_list` |
| ❌ Not closing strings (missing quotes) | SyntaxError | Always close strings with matching quotes |
| ❌ Using `is` instead of `==` | Compares identity, not value | Use `==` to check if values are the same |



