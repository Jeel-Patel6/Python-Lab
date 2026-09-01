#checking if a positive interger is prime or not
num = int(input("Please enter your number:"))

if num <=1:
    print("Not a prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
            print(f"{num} is a prime number")