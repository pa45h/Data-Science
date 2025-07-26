# ====================== 10. ADVANCED TOPICS ===========================

# Decorators allow behavior to be added to a function dynamically.
print("==== DECORATOR ====")


def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@decorator
def say_hi():
    print("Hi!")


say_hi()
print()


# Generators allow you to iterate over values lazily using 'yield'.
print("==== GENERATOR ====")


def generate_nums():
    for i in range(3):
        yield i


print(generate_nums())
for num in generate_nums():
    print(num)
print()

# ================= MULTITHREADING & MULTIPROCESSING =================
print("==== MULTITHREADING ====")
# Threading for running tasks in parallel (for I/O-bound tasks).
import threading
import time


# A CPU heavy calculation, just as an example. This can be anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, " is done")


def threaded(n):
    threads = []
    for i in range(n):
        t = threading.Thread(
            target=heavy,
            args=(
                500,
                i,
            ),
        )
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    start = time.time()
    threaded(80)
    end = time.time()
    print("Took: ", end - start)
print()


print("==== MULTIPROCESSING ====")
import time
import multiprocessing


# A CPU heavy calculation, just
# as an example. This can be
# anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")


def multiproc(n):
    processes = []
    for i in range(n):
        p = multiprocessing.Process(
            target=heavy,
            args=(
                500,
                i,
            ),
        )
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    start = time.time()
    multiproc(80)
    end = time.time()
    print("Took: ", end - start)
print()


# ========================= ASYNC / AWAIT ============================
print("==== ASYNC / AWAIT ====")
# Async IO allows concurrent execution of IO-bound operations.
import asyncio


async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


asyncio.run(greet())
print()


# =================== MODULES AND PACKAGES ===========================
print("==== MODULES AND PACKAGES ====")
# Importing a standard module.
import math

print(math.sqrt(16))  # Using math module to get square root

# Custom modules are your own Python files you can import and reuse.
print()


# =================== MEMORY MANAGEMENT ==============================
print("==== MEMORY MANAGEMENT ====")
import sys
import gc

x = [1, 2, 3, 4, 5]
print(sys.getsizeof(x))  # Get memory size of object

gc.collect()  # Force garbage collection
print()


# ================= TYPE HINTS / ANNOTATIONS =========================
print("==== TYPE HINTS / ANNOTATIONS ====")


def add(a: int, b: int) -> int:
    return a + b


print(add(3, 4))  # Helps with static type checking (e.g., using mypy)
print()


# ================== SERIALIZATION (Pickle / JSON) ===================
print("==== SERIALIZATION (Pickle / JSON) ====")
import pickle
import json

# Pickle: Python-specific serialization
obj = {"name": "Parth", "age": 20}
with open("data.pkl", "wb") as f:
    pickle.dump(obj, f)  # Serializing to binary

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
    print("pickle =", data)

# JSON: Language-independent serialization
json_data = json.dumps(obj)  # Convert dict to JSON string
print("json =", json_data)
print()


# ================== ENVIRONMENT VARIABLES ============================
print("==== ENVIRONMENT VARIABLES ====")
import os

os.environ["MY_ENV"] = "value"  # Setting an env variable
print(os.getenv("MY_ENV"))  # Accessing env variable
print()


# ================= PROFILING / PERFORMANCE ===========================
print("==== PROFILING / PERFORMANCE ====")

import time

# Simple timing using time.time()
start = time.time()

# Sum of first 10 million numbers (large enough to notice time, but not crash system)
sum_result = 0
for i in range(10_000_000):
    sum_result += i

end = time.time()

print("Execution Time using time.time():", end - start, "seconds\n")

# Advanced profiling using cProfile
import cProfile


# Function to compute sum using built-in range and sum (more efficient)
def compute():
    total = sum(range(1000))
    return total


# Profile the function using cProfile
print("Profiling using cProfile:")
cProfile.run("compute()")
print()
