Absolutely. Here's a **clean, beginner-friendly Day 3 note** that you can save as `Day3_Exception_Handling_Notes.md` or in your notebook.

---

# 📘 Day 3 Notes – Exception Handling & Logging

---

# 1. What is an Exception?

An **exception** is an error that occurs **while the program is running**.

Examples:

```python
10 / 0
```

```
ZeroDivisionError
```

```python
int("Hello")
```

```
ValueError
```

```python
numbers = [1, 2, 3]
print(numbers[10])
```

```
IndexError
```

Without exception handling, the program crashes.

---

# 2. `try`

The `try` block contains code that **might cause an error**.

### Syntax

```python
try:
    # Risky code
```

### Example

```python
try:
    print(10 / 2)
```

Output

```
5.0
```

If no error occurs, Python finishes the `try` block normally.

---

# 3. `except`

The `except` block runs **only if an exception occurs**.

### Syntax

```python
try:
    # Risky code
except ExceptionType:
    # Handle error
```

### Example

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output

```
Cannot divide by zero.
```

Instead of crashing, the program continues.

---

## Catch Specific Exceptions

✅ Good

```python
except ValueError:
```

❌ Avoid

```python
except:
```

Specific exceptions make debugging easier.

---

# 4. `else`

The `else` block runs **only if the `try` block succeeds without any exception**.

### Syntax

```python
try:
    ...
except:
    ...
else:
    ...
```

### Example

```python
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print(result)
```

Output

```
5.0
```

If an exception occurs, the `else` block is skipped.

---

# 5. `finally`

The `finally` block **always executes**, whether an exception occurs or not.

### Syntax

```python
try:
    ...
except:
    ...
finally:
    ...
```

### Example

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Division by zero")

finally:
    print("Program Finished")
```

Output

```
Division by zero
Program Finished
```

Use `finally` to:

* Close files
* Close database connections
* Disconnect APIs
* Free resources
* Print cleanup messages

---

# Execution Flow

### No Error

```
try
 ↓
else
 ↓
finally
```

---

### Error

```
try
 ↓
except
 ↓
finally
```

---

# 6. `raise`

`raise` is used to **create your own exception**.

Use it when your program detects invalid data.

### Syntax

```python
raise ExceptionType("Message")
```

### Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Output

```
ValueError: Age cannot be negative.
```

---

## Using `raise` with `try`

```python
try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as e:
    print(e)
```

Input

```
-5
```

Output

```
Age cannot be negative.
```

---

# `except ValueError as e`

`e` stores the exception object.

Example

```python
try:
    raise ValueError("Invalid Score")

except ValueError as e:
    print(e)
```

Output

```
Invalid Score
```

---

# 7. Logging

## What is Logging?

Logging is the **professional way to record information** about a program.

Instead of using

```python
print()
```

developers use

```python
logging
```

because logs can be:

* Saved to files
* Display different message levels
* Help debug applications
* Monitor AI models
* Track API calls

---

## Import

```python
import logging
```

---

## Basic Setup

```python
import logging

logging.basicConfig(level=logging.INFO)
```

---

## Logging Levels

### INFO

General information.

```python
logging.info("Training Started")
```

Output

```
INFO:root:Training Started
```

---

### WARNING

Something unexpected happened, but the program can continue.

```python
logging.warning("Learning rate is very high")
```

---

### ERROR

A serious error occurred.

```python
logging.error("Model failed to load")
```

---

### CRITICAL

A major failure.

```python
logging.critical("Database connection lost")
```

---

# Example

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program Started")
logging.warning("Battery Low")
logging.error("Invalid Input")
```

Output

```
INFO:root:Program Started
WARNING:root:Battery Low
ERROR:root:Invalid Input
```

---

# Logging vs Print

| print()                  | logging                            |
| ------------------------ | ---------------------------------- |
| Shows text on screen     | Records program events             |
| Cannot classify messages | Has INFO, WARNING, ERROR, CRITICAL |
| Mostly for debugging     | Used in professional applications  |
| Cannot easily save logs  | Can save logs to a file            |

---

# AI Example

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Loading Model...")

try:
    result = 10 / 0

except ZeroDivisionError:
    logging.error("Division by zero")
```

Output

```
INFO:root:Loading Model...
ERROR:root:Division by zero
```

---

# Complete Structure

```python
import logging

logging.basicConfig(level=logging.INFO)

try:
    # Risky Code

except ExceptionType:
    # Handle Error

else:
    # Runs if no exception occurs

finally:
    # Always executes
```

---

# Summary Table

| Keyword   | Purpose                     | Executes When                       |
| --------- | --------------------------- | ----------------------------------- |
| `try`     | Contains risky code         | Always                              |
| `except`  | Handles exceptions          | Only if an exception occurs         |
| `else`    | Runs if no exception occurs | After successful `try`              |
| `finally` | Cleanup code                | Always                              |
| `raise`   | Creates your own exception  | When your code detects invalid data |
| `logging` | Professional event tracking | Throughout the program              |

---

# 💡 AI Engineer Takeaways

* Use **`try`** to protect code that may fail (API calls, file reading, model loading).
* Use **specific `except` blocks** instead of a bare `except`.
* Use **`else`** for code that should run only after success.
* Use **`finally`** to clean up resources (files, network connections, databases).
* Use **`raise`** to reject invalid inputs before they cause bigger problems.
* Use **`logging`** instead of `print()` in real AI projects so you can monitor, debug, and audit your applications.

These concepts are fundamental in production AI systems, where code needs to be reliable, debuggable, and resilient to failures.
