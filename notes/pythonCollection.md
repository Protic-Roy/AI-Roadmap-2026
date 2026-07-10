## What is a List?

Imagine you're building an AI model to predict animals.

The model predicts:

cat
dog
cat
bird
dog

How do we store all these predictions?

Not like this:

prediction1 = "cat"
prediction2 = "dog"
prediction3 = "cat"
prediction4 = "bird"
prediction5 = "dog"

That would be a nightmare.

Instead we use one list.

predictions = [
    "cat",
    "dog",
    "cat",
    "bird",
    "dog"
]

A list stores multiple values inside one variable.

## 1. What is a Dictionary?

A dictionary stores data as key-value pairs.

Think of it like a real dictionary:

Word        Meaning
-----       -------
Python  →   Programming Language
AI      →   Artificial Intelligence

In Python:

student = {
    "name": "Roy",
    "age": 20,
    "department": "CSE"
}

Here:

Key           Value

"name"   ---> "Roy"
"age"    ---> 20
"department" -> "CSE"

Unlike a list, a dictionary does not use indexes.

Instead, you access data using its key.

Why AI Engineers Love Dictionaries

Imagine you ask ChatGPT:

"Who created Python?"

The API might return:

response = {
    "model": "gpt-4",
    "answer": "Guido van Rossum",
    "tokens": 35,
    "success": True
}

How do you get the answer?

print(response["answer"])

Output:

Guido van Rossum

Almost every AI API returns data like this (after JSON is converted to a Python dictionary).

2. Creating a Dictionary
student = {
    "name": "Roy",
    "age": 20,
    "cgpa": 3.85
}
3. Accessing Values
Method 1 ([])
print(student["name"])

Output:

Roy
But what if the key doesn't exist?
print(student["address"])

Python says:

KeyError

Your program crashes.

4. The Safer Way — .get()
print(student.get("address"))

Output:

None

Or provide a default:

print(student.get("address", "Unknown"))

Output:

Unknown
⭐ Why .get() Matters in AI

Imagine an API returns:

response = {
    "name": "Roy",
    "age": 20
}

Sometimes "email" isn't included.

This crashes:

print(response["email"])

But this is safe:

print(response.get("email", "No Email"))

Professional code almost always uses .get() when reading optional data from APIs.

5. Adding New Data
student["city"] = "Dhaka"

Now:

{
    "name": "Roy",
    "age": 20,
    "cgpa": 3.85,
    "city": "Dhaka"
}
6. Updating Data
student["cgpa"] = 3.95
7. Removing Data

Using pop():

student.pop("age")

Or:

del student["age"]
# 8. Useful Dictionary Methods
Keys
print(student.keys())

Output:

dict_keys(['name', 'cgpa', 'city'])
Values
print(student.values())

Output:

dict_values(['Roy', 3.95, 'Dhaka'])
Items
print(student.items())

Output:

dict_items([
    ('name','Roy'),
    ('cgpa',3.95),
    ('city','Dhaka')
])
# 9. Loop Through a Dictionary

Only keys:

for key in student:
    print(key)

Output:

name
cgpa
city

Keys and values:

for key, value in student.items():
    print(key, value)

Output:

name Roy
cgpa 3.95
city Dhaka

This is a very common pattern in AI code.

# 10. Dictionary Comprehension

Suppose:

numbers = [1,2,3,4]

Create:

{
    1:1,
    2:4,
    3:9,
    4:16
}

Using:

square = {x: x*x for x in numbers}

## 1. What is a Set?

A set is a collection of unique values.

Unlike a list:

❌ No duplicates
❌ No indexing
✅ Very fast searching

Example:

labels = {
    "cat",
    "dog",
    "bird"
}

Memory (conceptually):

{
 "cat",
 "dog",
 "bird"
}

Notice there are no indexes like labels[0].

Why AI Engineers Use Sets

Imagine an image dataset:

animals = [
    "cat",
    "dog",
    "cat",
    "bird",
    "dog",
    "cat",
    "horse"
]

How many different animals exist?

Without a set:

You'd have to write extra code.

With a set:

unique_animals = set(animals)

print(unique_animals)

Output:

{'cat', 'dog', 'bird', 'horse'}

Duplicates disappear automatically.

This is very common when finding unique labels in machine learning datasets.

2. Creating Sets
colors = {
    "Red",
    "Blue",
    "Green"
}

or

numbers = set([1,2,3,4])
⚠ Empty Set

Many beginners make this mistake.

This is NOT an empty set.

data = {}

This creates an empty dictionary.

To create an empty set:

data = set()

Remember this.

3. Adding Items
animals = {
    "cat",
    "dog"
}

animals.add("bird")

print(animals)

Output

{'cat','dog','bird'}
4. Duplicate Values
animals.add("dog")

Output

{'cat','dog','bird'}

Nothing changes.

A set never stores duplicates.

5. Removing Items
animals.remove("dog")

or

animals.discard("dog")
Difference

remove()

If the item doesn't exist

↓

❌ Error

discard()

If the item doesn't exist

↓

✅ Nothing happens

This makes discard() safer in some situations.

6. Membership Testing

This is one of the biggest advantages.

labels = {
    "cat",
    "dog",
    "bird"
}

print("dog" in labels)

Output

True

This lookup is very fast.

AI Performance Insight

Suppose you have one million labels.

Searching in a list:

if "dog" in labels_list:

Python checks:

cat?
dog?
bird?
horse?
...

One by one.

Average complexity:

O(n)

Searching in a set:

if "dog" in labels_set:

Python uses hashing, so it can usually find the item in constant time.

Average complexity:

O(1)

This is why sets are preferred for checking membership in large datasets.

7. Union
set1 = {
    "cat",
    "dog"
}

set2 = {
    "bird",
    "horse"
}

print(set1 | set2)

Output

{
'cat',
'dog',
'bird',
'horse'
}

Everything combined.

8. Intersection

Common items.

pets = {
    "cat",
    "dog",
    "fish"
}

farm = {
    "dog",
    "horse",
    "cow"
}

print(pets & farm)

Output

{'dog'}
9. Difference

Items only in the first set.

print(pets - farm)

Output

{
'cat',
'fish'
}

