# ===================== 08. ERROR HANDLING =============================
print("==== ERROR HANDLING ====")
# === Basic try-except-finally example ===
try:
    val = 10 / 0
except ZeroDivisionError:
    print("[Error] Cannot divide by zero!")
finally:
    print("[Finally] This always runs.")
print()

# === Catching multiple exception types ===
try:
    num = int("abc")  # ValueError
except ValueError:
    print("[Error] Invalid conversion to integer.")
except TypeError:
    print("[Error] Type mismatch.")
print()

# === Using else block: runs if no exception occurs ===
try:
    result = 10 / 2
except ZeroDivisionError:
    print("[Error] Division by zero.")
else:
    print("[Else] Division successful. Result =", result)
print()

# === Catching all exceptions generally (not recommended for production) ===
try:
    print(undefined_variable)  # type: ignore # NameError
except Exception as e:
    print("[General Exception] An error occurred:", e)
print()


# === Raising custom exceptions ===
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount


try:
    new_balance = withdraw(1000, 1500)
except ValueError as e:
    print("[Custom Error] Withdrawal failed:", e)
print()


# === Custom Exception class ===
class MyError(Exception):
    pass


try:
    raise MyError("Something custom went wrong!")
except MyError as e:
    print("[Custom Exception Class] Caught:", e)
print()

