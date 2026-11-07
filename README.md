# Introduction to Variables in Python

A variable is a name that refers to a value. Variables let a program remember information and use it later.

The [`variables_examples.py`](./variables_examples.py) file demonstrates the ideas in this guide using simple assignments and `print()` statements. It does not define any functions or use advanced Python features.

Run the examples with:

```bash
python variables_examples.py
```

## 1. Create a variable

Use the `=` sign to assign a value to a name:

```python
name = "Ana"
age = 20
```

Here, `name` refers to the text `"Ana"`, and `age` refers to the number `20`. Python creates each variable when it first appears on the left side of an assignment.

`print()` displays a value so you can see it:

```python
print(name)
print(age)
```

## 2. Change a variable

You can assign a different value to the same variable:

```python
score = 10
print(score)  # 10

score = 15
print(score)  # 15
```

After the second assignment, `score` refers to `15`.

## 3. Use variables in calculations

You can use variable values in arithmetic:

```python
apples = 3
more_apples = 2
total_apples = apples + more_apples

print(total_apples)  # 5
```

Python calculates the expression on the right side of `=` first, then assigns the result to the name on the left.

You can also use the current value of a variable to calculate a new one:

```python
coins = 5
coins = coins + 1

print(coins)  # 6
```

The shorter `+=` form does the same kind of update:

```python
coins = 5
coins += 1

print(coins)  # 6
```

## 4. Different kinds of values

A variable can refer to different kinds of values:

```python
city = "London"       # text
temperature = 18.5    # decimal number
is_sunny = False      # true-or-false value
```

Common value types include:

- Text, written inside quotes, such as `"London"`.
- Whole numbers, such as `20`.
- Decimal numbers, such as `18.5`.
- True-or-false values: `True` and `False`.

Python does not require you to write a type when creating a variable. The value determines its type.

## 5. Variable names

Choose names that explain what the values represent:

```python
student_name = "Ana"
number_of_books = 4
```

By convention, Python variable names use lowercase words separated by underscores (`snake_case`). Names cannot contain spaces or start with a number. Uppercase and lowercase letters are different, so `score` and `Score` are different names.

## 6. Assigning one variable to another

When you assign one variable to another, the second variable gets the current value:

```python
first_score = 10
second_score = first_score

first_score = 20

print(first_score)   # 20
print(second_score)  # 10
```

Changing `first_score` later does not change `second_score`.

## Remember

- `name = value` gives a value a name.
- `=` means assignment.
- A variable can be updated by assigning it a new value.
- Variables can be used in calculations.
- A clear name makes a program easier to understand.

## Practice

1. Create a variable for your favorite food and display it with `print()`.
2. Store two numbers in variables and assign their sum to a third variable.
3. Create a counter with the value `0`, add `1`, and display the new value.
4. Assign one number variable to another, then change the first one. Display both values.
