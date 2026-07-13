# 📌 Day 3 Mini Project: Model API Wrapper

> A beginner-friendly Python mini project to simulate real-world AI API behavior (including failures, retries, and logging).

---

## 🎯 Objective

Build a Python wrapper function that simulates calling an AI model API.

### Your wrapper should:

- Accept a user prompt
- Accept optional model settings via `**kwargs`
- Simulate API success/failure randomly
- Handle failures with exceptions
- Retry automatically (up to 3 attempts)
- Wait between retries (backoff)
- Log important events
- Return the final model response if successful

---

## 🌍 Why This Project Matters

In production apps, API calls are not always reliable.

Even if your code looks simple:

```python
response = model.generate(prompt)
```

real systems can fail due to:

- 🌐 Network issues
- ⏳ Timeout errors
- 🚫 Rate limits (`429`)
- 🔥 Temporary server overload
- 🔑 Invalid credentials

### ✅ Professional apps handle this gracefully

Instead of crashing, they:

1. Try the request
2. Catch errors
3. Retry with delay
4. Stop only after max retries

This project helps you practice exactly that.

---

## 📦 Functional Requirements

### 1) Prompt Input

Your function should accept a prompt string.

```python
call_model(prompt)
```

Example prompt:

```text
Hello AI
```

---

### 2) Optional Hyperparameters (`**hyperparams`)

Support optional keyword arguments like:

```python
call_model(
    "Hello AI",
    temperature=0.7,
    max_tokens=100
)
```

Inside the function, these should be available as a dictionary-like object.

---

### 3) Random API Failure Simulation

Since no real API is used, simulate random outcomes with Python’s `random` module:

- Success
- Failure

---

### 4) Exception Handling

On failure:

- Raise an exception
- Catch it with `try/except`
- Prevent crash

---

### 5) Retry Logic (Max: 3 Attempts)

If an attempt fails, retry automatically.

Example flow:

```text
Attempt 1 → Fail
Attempt 2 → Fail
Attempt 3 → Success
```

---

### 6) Backoff Between Retries

Use increasing wait times:

- Wait **1 second** before retry #2
- Wait **2 seconds** before retry #3

---

### 7) Logging (Use `logging`, not `print`)

Log all key events:

- API call started
- Attempt number
- Failure reason
- Retry action
- Success
- Final result / final failure

---

### 8) Return Final Response

On success, return a response value such as:

```text
Processed Prompt:
Hello AI
```

> Return it from the function (not just printing to console).

---

## ✅ Deliverable

A Python program that demonstrates a robust API wrapper simulation meeting all requirements above.

---

## 🧪 Suggested Test Cases

- Prompt succeeds on first attempt
- Prompt fails once, then succeeds
- Prompt fails all 3 attempts
- Hyperparameters are passed correctly
- Logs appear for each important step

---

## 📚 Skills Practiced

- Error handling with exceptions
- Retry & backoff strategy
- Logging best practices
- Writing resilient API wrappers

---

## 🏁 Completion Checklist

- [ ] Prompt accepted
- [ ] `**hyperparams` accepted
- [ ] Random failure simulation implemented
- [ ] Exceptions raised and handled
- [ ] Retry logic up to 3 attempts
- [ ] Delays between retries
- [ ] Proper logging used
- [ ] Successful response returned

---
import random
import time
import logging

print(random.random())
print(random.random())
print(random.random())

import time

print("Start")

time.sleep(3)

print("End")

logging.basicConfig(level=logging.INFO)

logging.info("Program Started")
logging.info("Calling API")
logging.info("Program Finished"
)


# 5
🎯 Goal of This Step

Right now, if call_model() fails:

API Call Failed
↓
ConnectionError
↓
Program Crashes ❌

We don't want that.

We want:

Attempt 1
     ↓
Fail
     ↓
Wait
     ↓
Attempt 2
     ↓
Fail
     ↓
Wait
     ↓
Attempt 3
     ↓
Success

This is called Retry Logic.

## FINISHED

# 🚀 Day 3 Mini Project — Model API Wrapper (Python)

Built a resilient Python wrapper that simulates real-world AI API behavior, including random failures, retry logic, and structured logging.

## 🔧 What I Implemented

- Prompt-based model call interface
- Optional hyperparameters using `**kwargs`
- Random API success/failure simulation
- Exception handling with `raise` + `try/except`
- Automatic retry mechanism (up to 3 attempts)
- Incremental backoff delays (`1s`, `2s`)
- Professional logging (`INFO`, `ERROR`, `CRITICAL`)
- Returned processed response on success

## ✅ Why This Matters

In production, external APIs can fail due to timeouts, rate limits, or network issues.  
This project demonstrates how to write code that **fails gracefully**, **retries safely**, and **does not crash**.

## 📚 Skills Demonstrated

- Python function design
- Error handling and control flow
- Retry/backoff patterns
- Logging best practices
- Writing robust API wrappers

## 🏁 Outcome

Completed a clean, beginner-friendly implementation of a fault-tolerant API wrapper pattern commonly used in real AI applications.