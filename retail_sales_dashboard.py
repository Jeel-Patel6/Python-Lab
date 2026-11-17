import csv
import matplotlib.pyplot as plt

products = []
sales = []

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        products.append(row["Product"])
        sales.append(float(row["Sales"]))

print("Retail Sales Data")

for i in range(len(products)):
    print(products[i], sales[i])

total = sum(sales)
average = total / len(sales)

print("Total Sales:", total)
print("Average Sales:", average)

# Bar Chart
plt.bar(products, sales)
plt.title("Retail Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# Line Chart
plt.plot(products, sales, marker="o")
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# Scatter Plot
plt.scatter(products, sales)
plt.title("Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()