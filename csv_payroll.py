import csv

def add():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Allowance: "))
    deduction = float(input("Enter Deduction: "))

    net_salary = basic + allowance - deduction

    with open("payroll.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([emp_id, name, basic, allowance, deduction, net_salary])

    print("Employee record added successfully!")


def display():
    try:
        with open("payroll.csv", "r") as file:
            reader = csv.reader(file)

            print("\n--- Employee Payroll Records ---")

            for row in reader:
                print("Employee ID:", row[0])
                print("Name:", row[1])
                print("Basic Salary:", row[2])
                print("Allowance:", row[3])
                print("Deduction:", row[4])
                print("Net Salary:", row[5])
                print("--------------------------")

    except FileNotFoundError:
        print("Payroll file does not exist.")

while True:
    print("\n1. Add Employee")
    print("2. Display Payroll Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()

    elif choice == "2":
        display()

    elif choice == "3":
        print("Exiting Payroll System...")
        break

    else:
        print("Invalid choice!")