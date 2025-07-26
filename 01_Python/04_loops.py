# =========================== 04. LOOPS ===============================

print("=== For Loop ===")
# For loop: commonly used for iterating over a range or sequence
for i in range(5):  # 0 to 4
    print("Value from range:", i)

# Printing all items in a shopping cart
cart = ["Apples", "Bananas", "Oranges"]
for item in cart:
    print("Cart item:", item)


print("\n=== While Loop ===")
# While loop: repeats as long as a condition is True
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# Retry connection attempts (max 3 times)
print("\nSimulating connection attempts:")
attempt = 1
connected = False
while attempt <= 3 and not connected:
    print(f"Attempt {attempt}: trying to connect...")
    # Simulating failure for first 2 attempts
    if attempt == 3:
        connected = True
        print("Connected successfully!")
    attempt += 1


print("\n=== Loop Control Statements ===")
# continue: skip current iteration
# break: exit the loop

print("Using continue and break:")
for i in range(6):
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking at 5")
        break
    print("i:", i)


# pass: a placeholder when no code is needed
print("\nUsing pass (does nothing):")
for i in range(3):
    if i == 1:
        pass  # No operation
    print("Processing i:", i)


print("=== Loop with ELSE ===")
# FOR loop with else: executes else if loop completes without break
for i in range(5):
    print("i =", i)
else:
    print("For loop completed without break.\n")


# WHILE loop with else
x = 0
while x < 3:
    print("x =", x)
    x += 1
else:
    print("While loop ended normally.\n")


# Loop with else and break
for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)
else:
    print("This won't print because loop was broken.\n")
print()

print("=== Loop Comprehensions ===")
# List comprehension
squares = [x**2 for x in range(5)]
print("Squares (List):", squares)

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "banana", "kiwi"]}
print("Set of word lengths:", unique_lengths)

# Dictionary comprehension
square_dict = {x: x**2 for x in range(4)}
print("Squares (Dict):", square_dict)

# Conditional comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)
print()


# 1. Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Final count of Positive number is: ", positive_number_count)
print()

# 2. Calculate the sum of even numbers up to a given number n.
n = 10
sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += 1

print("Sum of even number is: , ", sum_even)
print()

# 3. Print the multiplication table for a given number up to 10, but skip the fifth iteration.
number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(number, "x", i, "=", number * i)
print()

# 4. Reverse a string using a loop.
input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str

print(reversed_str)
print()

# 5. Given a string, find the first non-repeated character.
input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break
print()

# 6. Compute the factorial of a number using a while loop.
number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)
print()

# 7. Keep asking the user for input until they enter a number between 1 and 10.
while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")
print()

# 8. Check if a number is prime.
number = 28
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)
print()

# 9. Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)
print()

# 10. Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(
        "Attempt",
        attempts + 1,
        "- wait time",
        wait_time,
    )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
print()
