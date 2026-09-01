num = int(input("Enter your number:"))

if(num<0):
    print("Factorial does not exsist for negative numbers")
else:
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i

print(f"The factorial of {num} is {factorial}")