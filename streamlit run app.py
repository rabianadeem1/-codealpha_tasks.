import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 330,
    "AMZN": 140,
    "GOOGL": 130
}

def stock_portfolio_tracker():
    portfolio = {}
    total_value = 0

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not available. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_value += stock_prices[stock] * quantity

    print("\n=== Portfolio Summary ===")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        print(f"{stock}: {qty} shares → ${value}")

    print(f"\nTotal Investment Value: ${total_value}")

    # Option to save result
    save_option = input("\nDo you want to save results? (y/n): ").lower()
    if save_option == "y":
        file_type = input("Save as .txt or .csv? ").lower()
        
        if file_type == "txt":
            with open("portfolio.txt", "w") as f:
                f.write("=== Portfolio Summary ===\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock}: {qty} shares -> ${stock_prices[stock] * qty}\n")
                f.write(f"\nTotal Investment Value: ${total_value}")
            print("✅ Saved as portfolio.txt")

        elif file_type == "csv":
            with open("portfolio.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Value"])
                for stock, qty in portfolio.items():
                    writer.writerow([stock, qty, stock_prices[stock] * qty])
                writer.writerow(["TOTAL", "", total_value])
            print("✅ Saved as portfolio.csv")

        else:
            print("❌ Invalid file type. Skipping save.")

# Run program
stock_portfolio_tracker()
