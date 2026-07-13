# AI Roadmap 2026

My 4-month journey into AI Engineering, Data Science, and Hackathons.

## Goals

- Learn Python
- Learn Machine Learning
- Learn Deep Learning
- Build AI Projects
- Participate in AI Hackathons
 
 # Day 1
✅ Set up a proper Python development environment.
✅ Used Git and GitHub.
✅ Built a command-line application.
✅ Learned about secure configuration with .env.
✅ Used Ruff to check your code style

# Day 2
Python Collections
✅ Lists
✅ Dictionaries
✅ Sets
Pythonic Features
✅ List Comprehensions
✅ Dictionary Comprehensions
✅ zip()
✅ enumerate()
✅ Basic unpacking (a, b = ...)
✅ join()
Mini Project
✅ Hackathon Team Builder

# 📅 Day 3 Summary — Functions & Error Handling

I covered much more than just writing functions.  
**Day 3 was about learning how to write robust, reusable Python code** — the kind I'll need for AI engineering and hackathons.

---

## 1) Functions ✅

I learned how to create reusable blocks of code.

```python
def greet(name):
    return f"Hello {name}"
```

### I now understand:

- `def`
- Parameters
- Arguments
- `return`
- Why functions are better than repeating code

---

## 2) Default Arguments ✅

```python
def greet(name="Guest"):
    print(name)
```

If no value is passed, Python uses the default.

---

## 3) `*args` ✅

```python
def average(*numbers):
    return sum(numbers) / len(numbers)
```

I learned:

- Accept any number of positional arguments
- `*args` is stored as a **tuple**

Example:

```python
average(10, 20, 30, 40)
```

---

## 4) `**kwargs` ✅

```python
def train_model(**params):
    print(params)
```

I learned:

- Accept any number of keyword arguments
- `**kwargs` is stored as a **dictionary**

Example:

```python
train_model(
    learning_rate=0.01,
    epochs=20
)
```

Output:

```python
{
    "learning_rate": 0.01,
    "epochs": 20
}
```

I also saw why AI libraries use this pattern.

---

## 5) Variable Scope (LEGB) ✅

Python searches variables in this order:

```text
Local
↓
Enclosing
↓
Global
↓
Built-in
```

I practiced:

- Local variables
- Nested functions
- Global variables
- Variable shadowing

---

## 6) Error Handling ✅

I learned:

```python
try:
```

Run risky code.

```python
except:
```

Catch errors.

```python
else:
```

Run only if no error occurs.

```python
finally:
```

Always runs.

---

## 7) `raise` ✅

Instead of:

```python
print("Error")
```

you learned:

```python
raise ConnectionError("API Failed")
```

This tells Python something actually went wrong.

---

## 8) Logging ✅

Instead of `print()`, I used logging levels:

```python
logging.info()
logging.error()
logging.critical()
```

I now know:

- `INFO` → General progress
- `WARNING` → Something unusual
- `ERROR` → An operation failed
- `CRITICAL` → The program cannot continue

---

## 9) Retry Logic ✅

I built:

```python
for attempt in range(1, 4):
```

Instead of crashing immediately, my program retries.

This is commonly used when:

- AI APIs are temporarily unavailable
- Network requests fail
- Rate limits are reached

---

## 10) `time.sleep()` ✅

```python
time.sleep(attempt)
```

My program waits before retrying, preventing rapid repeated requests.
## 📚 Topics Covered

- ✅ Functions and `return`
- ✅ Default Arguments
- ✅ `*args` and `**kwargs`
- ✅ LEGB Variable Scope (Local, Enclosing, Global, Built-in)
- ✅ `try`, `except`, `else`, and `finally`
- ✅ Raising Exceptions with `raise`
- ✅ Python Logging (`logging.info`, `logging.error`, `logging.critical`)
- ✅ Retry Logic using `for` loops
- ✅ `time.sleep()` for retry delays

