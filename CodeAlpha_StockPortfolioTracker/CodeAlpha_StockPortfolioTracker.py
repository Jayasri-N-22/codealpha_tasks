"""
Task 2: Stock Portfolio Tracker
"""
stocks={"AAPL":180,
        "TSLA":250,
        "MSFT":420,
        "GOOG":170,
        "AMZN":190
        }
total=0

print("Stock Portfolio Tracker")
print("-----------------------")

while True:
    stock=input("Enter stock name (or type 'done' to finish):").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity= int(input("Enter quantity: "))

        investment=stocks[stock]*quantity
        total=total+investment

        print("Stock price:",stocks[stock])
        print("Investment:",investment)

    else:
        print("Stock not found.")

print("\nTotal Investment Value:",total)

