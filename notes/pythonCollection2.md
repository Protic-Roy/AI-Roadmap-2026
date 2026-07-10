## What is a Comprehension?

A comprehension is a shorter, cleaner way to create a new collection (list or dictionary) from an existing one.

Instead of writing 5–6 lines, you can often write one readable line.

Before Comprehensions (Traditional Way)

Suppose you want the squares of numbers from 0 to 9.

squares = []

for i in range(10):
    squares.append(i * i)

print(squares)

Output:

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Using a List Comprehension

The same thing becomes:

squares = [i * i for i in range(10)]

print(squares)

Exactly the same output.

Understanding the Syntax

General form:

new_list = [expression for item in iterable]

Break it down:

[i * i for i in range(10)]
Part	Meaning
i * i	What you want to put into the new list
for i	Loop variable
in range(10)	The data you're looping through

Think of it like reading English:

"Create a list containing i*i for every i in range(10)."

Example 2

Double every number.

Traditional:

numbers = [1,2,3,4]

double = []

for n in numbers:
    double.append(n*2)

print(double)

Comprehension:

numbers = [1,2,3,4]

double = [n*2 for n in numbers]

print(double)

Output:

[2,4,6,8]
Example 3 (Strings)
names = ["roy","alice","bob"]

upper_names = [name.upper() for name in names]

print(upper_names)

Output:

['ROY','ALICE','BOB']
Conditions Inside Comprehensions

Suppose we only want even numbers.

Traditional:

numbers = []

for i in range(10):
    if i % 2 == 0:
        numbers.append(i)

print(numbers)

Comprehension:

numbers = [i for i in range(10) if i % 2 == 0]

print(numbers)

Output:

[0,2,4,6,8]

The if comes at the end.

AI Example

Suppose your model predicts:

predictions = [
    "cat",
    "dog",
    "bird",
    "dog",
    "horse"
]

Convert everything to uppercase:

upper_predictions = [label.upper() for label in predictions]

print(upper_predictions)

Output:

['CAT','DOG','BIRD','DOG','HORSE']
Dictionary Comprehension

General form:

{key_expression: value_expression for item in iterable}

Example:

numbers = [1,2,3,4]

square = {x: x*x for x in numbers}

print(square)

Output:

{
1:1,
2:4,
3:9,
4:16
}
Why AI Engineers Use Comprehensions

Imagine you have prediction probabilities:

probabilities = [0.91,0.22,0.88,0.63]

Convert them into percentages:

percentages = [p*100 for p in probabilities]

Or clean text:

words = [" AI "," Python "," Data "]

clean = [w.strip() for w in words]

This is common in preprocessing before training models.