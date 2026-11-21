a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Arithmetic operations
print("\n--- Arithmetic Operations ---")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
    print("Floor Division =", a // b)
    print("Remainder =", a % b)
else:
    print("Division is not possible")
    print("Floor Division is not possible")
    print("Remainder is not possible")

# Comparison operations
print("\n--- Comparison Operations ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)