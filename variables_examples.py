"""Run beginner-friendly examples of Python variables.

Run this file with:
    python variables_examples.py
"""


def calculate_double(number):
    """Return twice the given number."""
    result = number * 2
    return result


def greet():
    message = "Hello"
    print(message)


def main():
    print("PYTHON VARIABLES: EXAMPLES")
    print("=" * 36)

    print("\n1. CREATING VARIABLES")
    name = "Ana"
    age = 20
    height = 1.65
    is_learning = True
    print("Name:", name)
    print("Age:", age)
    print("Height:", height)
    print("Is learning:", is_learning)
    print("The name is associated with:", name)

    print("\n2. ASSIGNMENT AND REASSIGNMENT")
    score = 10
    another_score = score
    print("Score:", score)
    print("Another name for the same integer value:", another_score)
    score = 15
    print("Score after reassignment:", score)
    print("Another score remains:", another_score)

    print("\n3. CALCULATIONS AND COMPARISON")
    total = 7
    total = total + 3
    print("After total = total + 3:", total)
    total += 2
    total -= 1
    total *= 3
    print("After += 2, -= 1, and *= 3:", total)
    answer = 5
    print("answer == 5:", answer == 5)

    print("\n4. TYPES AND DYNAMIC TYPING")
    quantity = 4
    price = 2.5
    product = "bread"
    available = True
    result = None
    print("quantity:", quantity, type(quantity))
    print("price:", price, type(price))
    print("product:", product, type(product))
    print("available:", available, type(available))
    print("result:", result, type(result))

    data = 12
    print("data before reassignment:", data, type(data))
    data = "twelve"
    print("data after reassignment:", data, type(data))
    number_from_text = int("12")
    print('int("12") + 3:', number_from_text + 3)

    print("\n5. READING USER INPUT")
    user_name = input("What is your name? ")
    age_text = input("How old are you? ")
    try:
        user_age = int(age_text)
    except ValueError:
        print(f"{age_text!r} is not a valid integer; skipping the age calculation.")
    else:
        print(f"Hello, {user_name}. Next year you will be {user_age + 1}.")

    print("\n6. READABLE VARIABLE NAMES")
    full_name = "Ana Ruiz"
    number_of_attempts = 3
    print("full_name:", full_name)
    print("number_of_attempts:", number_of_attempts)
    print("Names are case-sensitive:", "name" != "Name")

    print("\n7. MUTABLE OBJECTS AND REFERENCES")
    fruits = ["apple", "pear"]
    my_fruits = fruits
    my_fruits.append("grape")
    print("Original list after changing its alias:", fruits)

    copied_fruits = fruits.copy()
    copied_fruits.append("orange")
    print("Original list after changing the copy:", fruits)
    print("Shallow copy:", copied_fruits)

    print("\n8. FUNCTION SCOPE AND RETURN VALUES")
    greet()
    doubled = calculate_double(6)
    print("Double of 6:", doubled)

    print("\n9. CONSTANTS BY CONVENTION")
    TAX_RATE = 0.19
    print("TAX_RATE:", TAX_RATE)
    print("Uppercase is a convention, not runtime enforcement.")

    print("\n10. TYPE ANNOTATIONS")
    annotated_age: int = 20
    print("Annotated age:", annotated_age, type(annotated_age))
    annotated_age = "twenty"
    print("After assigning text, annotations do not convert values:", annotated_age)

    print("\nEnd of examples.")


if __name__ == "__main__":
    main()
