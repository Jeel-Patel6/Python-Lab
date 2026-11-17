products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse"]

sales = [50000, 30000, 5000, 3000, 1500]

prices = (50000, 15000, 2500, 1500, 500)

sales_data = {
    "Laptop": 50000,
    "Mobile": 30000,
    "Headphones": 5000,
    "Keyboard": 3000,
    "Mouse": 1500
}

total_sales = sum(sales)

print("----- SALES DATA ANALYZER -----")

print("\nProduct Sales:")

for i in range(len(products)):
    print(products[i], ":", sales[i])

highest = max(sales)
lowest = min(sales)

print("\nTotal Sales:", total_sales)
print("Highest Sales:", highest)
print("Lowest Sales:", lowest)

average = total_sales / len(sales)

print("Average Sales:", average)

index = sales.index(highest)

print("Best Selling Product:", products[index])

print("\nSales Performance:")

if total_sales >= 100000:
    print("Excellent Sales")
elif total_sales >= 50000:
    print("Good Sales")
else:
    print("Low Sales")

print("\nSales Dictionary:")
print(sales_data)
