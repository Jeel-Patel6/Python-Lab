
import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

op = int(input("Enter operation: "))

if op == 1:
    print("Result =", a + b)
elif op == 2:
    print("Result =", a - b)
elif op == 3:
    print("Result =", a * b)
elif op == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")


print("\n1. Area of Rectangle")
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle =", area)

print("\n2. Area of Circle")
radius = float(input("Enter radius: "))
area_c = math.pi * radius * radius
print("Area of Circle =", area_c)