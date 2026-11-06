stock_prices = {
    "VANDU": 180,
    "BHARTI": 250,
    "PRATISHTHA": 170,
    "PRASHANT": 420
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("\nAvailable stocks and prices:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price} per share")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose an available stock.")
        continue

    try:
        quantity = int(input("Enter quantity of shares: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid whole number.")

print("\n===== Your Portfolio =====")

report = ["Stock Portfolio Tracker", ""]

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    line = f"{stock}: {quantity} shares x ${price} = ${investment}"
    print(line)
    report.append(line)

print(f"\nTotal Investment: ${total_investment}")
report.append(f"\nTotal Investment: ${total_investment}")

save = input("\nSave report to a text file? (yes/no): ").strip().lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("\n".join(report))

    print("Report saved successfully as portfolio.txt")

print("\nThank you for using the Stock Portfolio Tracker!")
