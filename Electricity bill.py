import math

print("=======karnataka electricity=========")

name = input("Enter your name: ")
id = int(input("Enter your customer ID: "))
prev = int(input("Enter your previous meter reading: "))
next = int(input("Enter your current meter reading: "))
cost = int(input("Enter the cost per unit: "))

print(f"Welcome {name}, ID {id}")
print("================================")
print(f"Total units consumed : {next-prev}")
print(f"Enery charge : {cost*(next-prev)}")
print(f"Energy Duty : {0.05*cost*(next-prev)}")
print("The fixed meter charge is 100")
print(f"Net Bill : {100 + (cost*(next-prev)) + (0.05*cost*(next-prev))}")
print("================================")
print("Clear the bill by end of current month to avoid power cuts")