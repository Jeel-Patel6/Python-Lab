class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display(self):
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


name = input("Enter name: ")
acc = input("Enter account number: ")
balance = float(input("Enter opening balance: "))

account = BankAccount(name, acc, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display()

    elif choice == "4":
        break

    else:
        print("Invalid choice")