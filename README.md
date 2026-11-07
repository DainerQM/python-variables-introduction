# Introduction to Variables in Python

A variable gives a name to a value so that your program can use and work with it. This guide explains how variables are created and updated, and how they relate to Python objects.

## 1. Creating a variable

In Python, a variable is created when you assign a value to a name:

```python
name = "Ana"
age = 20
height = 1.65
is_learning = True
```

The `=` sign is the assignment operator: it assigns the value on its right to the name on its left. Python does not require a special declaration keyword or a type to be written in advance.

```python
score = 10
```

Here, `score` is the name and `10` is the assigned value.

## 2. What happens when you assign a value

It is useful to think of a variable as a name associated with an object, not as a box that permanently contains one data type. When Python evaluates `score = 10`, it makes the name `score` refer to the object represented by `10`.

```python
score = 10
another_score = score

print(score)          # 10
print(another_score)  # 10
```

The second assignment makes both names refer to the value `10`. Reassigning one name later does not automatically reassign the other:

```python
score = 10
another_score = score
score = 15

print(score)          # 15
print(another_score)  # 10
```

## 3. Reassignment and calculations

A variable can receive another value later. This is called reassignment:

```python
temperature = 18
temperature = 22
print(temperature)  # 22
```

You can also use its current value to calculate a new one:

```python
total = 7
total = total + 3
print(total)  # 10
```

Python evaluates the expression on the right first, then assigns its result back to `total`. For common operations, augmented assignment operators are available:

```python
total = 7
total += 2  # equivalent to total = total + 2
total -= 1  # equivalent to total = total - 1
total *= 3  # equivalent to total = total * 3
```

Do not confuse assignment with comparison. `=` assigns a value; `==` checks whether two values are equal:

```python
answer = 5
print(answer == 5)  # True
```

## 4. Value types and dynamic typing

Every object has a type. For example:

```python
quantity = 4           # int: an integer
price = 2.5            # float: a floating-point number
product = "bread"      # str: text
available = True       # bool: true or false
result = None          # NoneType: an intentional absence of a value
```

Use `type()` to inspect a value's type:

```python
quantity = 4
product = "bread"
print(type(quantity))  # <class 'int'>
print(type(product))   # <class 'str'>
```

Python is dynamically typed: a name can be reassigned to an object of a different type. This does not mean Python ignores types; operations still depend on the objects' types:

```python
data = 12
data = "twelve"
```

Reassignment is valid, although changing a variable's type without a clear reason can make a program harder to understand. Some operations between different types are not valid:

```python
# "12" is text, not a number:
# print("12" + 3)  # TypeError

number = int("12")
print(number + 3)  # 15
```

## 5. Reading input from the user

The `input()` function always returns text (`str`), even when the user types digits. Convert the result when you need another type:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello, {name}. Next year you will be {age + 1}.")
```

If the text does not represent a valid integer, `int()` raises a `ValueError`. Programs that process real input should validate or handle that case.

## 6. Valid and readable names

Variable names:

- Can contain letters, numbers, and underscores (`_`).
- Cannot start with a number.
- Cannot contain spaces or be Python keywords such as `if`, `class`, or `for`.
- Are case-sensitive: `name`, `Name`, and `NAME` are different names.

Choose descriptive names and, by convention, use `snake_case`:

```python
full_name = "Ana Ruiz"
number_of_attempts = 3
```

Avoid overly generic names (`x`, `data`) when a more specific name explains the purpose. Do not use the names of built-in functions or types, such as `list` or `str`, because that would hide those built-ins in that scope.

## 7. Variables that refer to mutable objects

Numbers, strings, and booleans are immutable: they are not changed in place; an operation produces a value, and a variable can be reassigned. Lists and dictionaries, on the other hand, are mutable: their contents can change.

Assigning a list to another name does not automatically create a second list:

```python
fruits = ["apple", "pear"]
my_fruits = fruits

my_fruits.append("grape")
print(fruits)  # ['apple', 'pear', 'grape']
```

Both names refer to the same list, so a change made through one name is visible through the other. To create a shallow copy of a list, use `copy()`:

```python
fruits = ["apple", "pear"]
my_fruits = fruits.copy()
my_fruits.append("grape")

print(fruits)     # ['apple', 'pear']
print(my_fruits)  # ['apple', 'pear', 'grape']
```

A shallow copy creates a new list but does not recursively copy mutable objects that the list may contain.

## 8. Scope: where a name exists

A local variable created inside a function can be used inside that function:

```python
def greet():
    message = "Hello"
    print(message)

greet()
# print(message)  # NameError: message is not defined in this scope
```

Function parameters are also local names. Passing required data as parameters and returning results with `return` is preferable to depending on global variables:

```python
def calculate_double(number):
    result = number * 2
    return result

double = calculate_double(6)
print(double)  # 12
```

## 9. Constants by convention

Python does not prevent a variable from being reassigned. To indicate that a value is intended to be a constant, the convention is to write its name in uppercase with underscores between words:

```python
TAX_RATE = 0.19
```

Uppercase names are a convention for people reading the code; they do not make a value immutable.

## 10. Type annotations

Annotations can document an expected type and help analysis tools, but by themselves they do not convert or validate the value at runtime:

```python
age: int = 20
name: str = "Ana"
```

Python will still execute an assignment of a different type if the program makes one. Use conversions, validation, or type-checking tools when you need to verify data.

## Summary

- An assignment such as `name = value` associates a name with the result of an expression.
- A name can be reassigned, including to an object of a different type.
- Objects have types, and their types determine which operations are valid.
- Two names can refer to the same mutable object; changes can be visible through both names.
- Names defined inside a function have local scope.
- Type annotations and uppercase names document intent but do not enforce types or constants by themselves.

## Practice

1. Create variables for a book's title, price, and availability.
2. Increase a counter with `+= 1` and print its new value.
3. Ask the user for two integers and print their sum. Remember that `input()` returns text.
4. Assign a list to two names, append an item through one name, and observe the list through the other.

Run each example separately in Python and change the values to see how the program behaves.

## Python examples

The accompanying [`variables_examples.py`](./variables_examples.py) file runs examples for the topics in this guide. Run it from a terminal:

```bash
python variables_examples.py
```

The input example asks for a name and age. If the age is not a valid integer, the script reports the error and continues with the remaining examples.
