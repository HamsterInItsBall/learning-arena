# **Python Conditionals - Expanded Learning Notes**

---

## What Are Conditionals?

Conditionals are Python’s way of **making decisions**.  
They let me write code that **reacts differently** based on **True** or **False** checks.

Example:
- "If it's raining, take an umbrella."
- "If I'm hungry, eat lunch."

---

## Python’s Basic Conditional: **if Statement**

Python's `if` statement allows **decision-making** based on **Boolean conditions**. 
If the condition evaluates to **True**, Python executes the indented block. 
If **False**, Python skips it.

#### **Example:**
```python
x = 5
y = 10

if x < y:
    print("x is less than y")
```
#### Basic Syntax
```python
if <condition>:
    <indented statement(s)>
```
**When to use it:**
- Anytime you need your code to **react differently** based on a condition.
- Example: Show a discount only if the user is a member.
- Example: Display a warning if an input is invalid.

---
## **Grouping Statements: Indentation and Blocks**
### **Python: It’s All About the Indentation**
Python uses **indentation** to define **code blocks**. 
Indentation must be **consistent**—mixing spaces and tabs causes errors.

#### **Example:**
```python
if True:
    print('Inside block')
print('Outside block')
```
### **What Do Other Languages Do?**

Languages like **C, C++, Java, and Perl** use **curly braces** `{}` to define blocks:
```python
if (condition) {
    // code block
}
```

### **Which Is Better?**
**Pros of Python’s Indentation:**
- Cleaner and easier to read
- Forces consistency
- Prevents misleading indentation

**Cons:**
- Some dislike being forced into one style
- Editors mixing spaces and tabs can cause hidden bugs
Despite this, Python's indentation promotes **highly readable code**.

**When to use it:**
- **Every time you write a control structure** (if, for, while, etc.).
- Indentation tells Python **which lines to execute together**.
---

## **The `else` and `elif` Clauses**
### `else` Clause
Runs when the `if` condition is **False**.
```python
x = 20
if x < 50:
    print('x is small')
else:
    print('x is large')
```
### `elif` Clause
Checks **additional conditions** if the previous `if` was **False**.
```python
name = 'Ron'
if name == 'Harry':
    print('Hello Harry')
elif name == 'Ron':
    print('Hello Ron')
else:
    print("I don't know who you are")
```
Python stops checking after the **first match.**

**Why they exist:**
- `if` only checks *8one condition**.
- `else` allows you to define **what happens when the condition is false**.
- `elif` lets you **check multiple conditions in order**.

**When to use them:**
- `else`: To **cover all other possibilities** when your main condition is false.
- `elif`: To **check several conditions** without writing nested `if` statements.
---

## **One-Line if Statements**
Python supports **single-line** `if` **statements**:
```python
if True: print('Quick check')
```
Multiple actions on one line are **allowed but discouraged**:
```python
if True: print('A'); print('B')
```
PEP 8 recommends avoiding this for **readability**.

**When to use them:**
- Only for **simple, short** actions.
- Avoid overusing them, especially for complex logic.
---

## Conditional Expressions (Ternary Operator)

Python's **ternary operator** is written as:
```python
<result_if_true> if <condition> else <result_if_false>
```
**Why it exists:**
- Lets you **choose a value** based on a condition in one line.
- Helps **simplify assignments** without writing full `if` blocks.

**When to use it:**
- When you want to **set a variable** based on a **simple condition**.
    
#### Example:
```python
raining = False
activity = 'beach' if not raining else 'library'
print('Let’s go to the', activity)
```
Python evaluates **the middle condition first** and returns **one of the two results**.

#### Chained Example:
```python
status = ('child' if age < 13 else 'teen' if age < 20 else 'adult')
```
Be cautious—**deep nesting** reduces clarity.

#### Example:
```python
access = "granted" if user == "admin" else "denied"
```
**Don’t** overuse it when you have many conditions—use `if-elif-else` instead.

---

## **The Python pass Statement**

`pass` acts as a **placeholder** when no action is needed yet.

**When to use it:**
- **While building structure**, before writing the actual logic.
- In **empty classes, functions, or loops** you plan to complete later.
- **Code stubs** during development

#### Example:
```python
if True:
    pass

print('Program continues')
```
**Remember to replace** it with real code when you’re ready.

---

## **Common Pitfalls and Beginner Mistakes with Examples**

| **Mistake**                                  | **What Happens**                              | **Incorrect Example**                              | **Correct Example**                              |
|----------------------------------------------|-----------------------------------------------|----------------------------------------------------|--------------------------------------------------|
| ❌ Forgetting the colon `:`                   | SyntaxError                                  | `if True print("Yes")`                            | `if True: print("Yes")`                          |
| ❌ Mixing tabs and spaces                    | IndentationError                             | _Mixing spaces and tabs in the same file_          | _Use 4 spaces consistently for indentation_      |
| ❌ Misaligned indentation                    | Unexpected IndentationError                   | ```\nif True:\n print(\"A\")\n  print(\"B\")\n``` | ```\nif True:\n    print(\"A\")\n    print(\"B\")\n``` |
| ❌ Writing `else if` instead of `elif`       | SyntaxError                                  | ```\nif x == 1:\n    print(\"One\")\nelse if x == 2:\n    print(\"Two\")\n``` | ```\nif x == 1:\n    print(\"One\")\nelif x == 2:\n    print(\"Two\")\n``` |
| ❌ Using `=` instead of `==` in conditions   | Always evaluates as True and reassigns value  | ```\nif x = 5:\n    print(\"x is five\")\n```     | ```\nif x == 5:\n    print(\"x is five\")\n```    |
| ❌ Overusing one-liners                      | Hard-to-read code                            | `if True: print("A"); print("B")`                  | ```\nif True:\n    print(\"A\")\n    print(\"B\")\n``` |
| ❌ Using `pass` when logic is actually needed| Silently does nothing                        | ```\nif condition:\n    pass\n```                 | ```\nif condition:\n    print(\"Do something\")\n``` |
| ❌ Forgetting to cover all outcomes          | Program may miss handling some conditions     | ```\nif x == 1:\n    print(\"One\")\n```          | ```\nif x == 1:\n    print(\"One\")\nelse:\n    print(\"Not One\")\n``` |
| ❌ Over-nesting ternary operators            | Confusing and unreadable logic                | ```\nstatus = \"A\" if x == 1 else \"B\" if x == 2 else \"C\"\n``` | ```\nif x == 1:\n    status = \"A\"\nelif x == 2:\n    status = \"B\"\nelse:\n    status = \"C\"\n``` |
