# ========================== 05. FUNCTIONS =============================

# 1. Basic Function
print("==== Functions ==== ")


def greet(name):
    return f"Hello, {name}!"


print(greet("Parth"))  # Hello, Parth!
print()


# 2. Function with Default Argument
def describe(name, age=18):
    print(f"{name} is {age} years old.")


describe("Parth")  # Default age
describe("pa45h", age=20)  # Custom age
print()

# 3. Keyword Arguments
describe(age=21, name="Jay")  # Order doesn't matter
print()


# 4. Variable-length Arguments (*args)
def print_fruits(*fruits):
    print("You like:")
    for fruit in fruits:
        print(fruit)


print_fruits("Apple", "Banana", "Cherry")
print_fruits("Apple", "Banana", "Cherry", "Apple", "Banana", "Cherry")
print()


# 5. Variable-length Keyword Arguments (**kwargs)
def student_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


student_details(name="Parth", age=20, branch="CE")
print()

# 6. Lambda (Anonymous) Function
square = lambda x: x**2
print("Square of 5 is:", square(5))
print()


# 7. Passing Function as Argument
def apply_operation(func, value):
    return func(value)


print("Cube using lambda:", apply_operation(lambda x: x**3, 3))
print()


# 8. Nested Function
def outer():
    def inner():
        print("Inner function called")

    print("Calling inner from outer:")
    inner()


outer()
print()


# 9. Return Multiple Values
def min_max(numbers):
    return min(numbers), max(numbers)


mn, mx = min_max([3, 7, 1, 9])
print("Min:", mn, "Max:", mx)
print()


# 10. Function with yield
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


for num in even_generator(10):
    print(num)
print()


# 11. Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5 is:", factorial(5))
print()


# 12. Higher-order Functions: map, filter, reduce:
nums = [1, 2, 3, 4, 5]
print(f"nums{nums}")
# map: square each number
squares = list(map(lambda x: x**2, nums))
print("Squares using map:", squares)
print()

# filter: even numbers only
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter:", evens)
print()

# reduce: product of all numbers
from functools import reduce

product = reduce(lambda x, y: x * y, nums)
print("Product using reduce:", product)
print()
