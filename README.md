Got it ✅ Let’s create a **README.md** for your `StockPortfolioTracker` project so it looks nice on GitHub.

Here’s a simple but professional version:

````markdown
# 📊 Stock Portfolio Tracker

A simple **Stock Portfolio Tracker** built with Python.  
It allows you to input stocks and quantities, calculates the **total investment value**, and lets you **save results** as `.txt` or `.csv`.

---

## 🚀 Features
- Hardcoded stock prices (e.g., AAPL, TSLA, MSFT, AMZN, GOOGL).
- User can input:
  - Stock name (symbol)
  - Quantity of shares
- Portfolio summary with **per-stock value** and **total investment**.
- Option to **save results**:
  - `.txt` file
  - `.csv` file
- Error handling for wrong inputs.

---

## 🛠️ Tech Used
- **Python 3**
- Dictionaries (to store stock prices)
- File handling (`.txt`, `.csv`)
- Optional: **Streamlit** for interactive UI

---

## 📥 Installation
1. Clone this repo:
   ```bash
   git clone https://github.com/rabianadeem1/-codealpha_tasks.git
   cd -codealpha_tasks/StockPortfolioTracker
````

2. (Optional) Install dependencies if using **Streamlit**:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the program:

```bash
python app.py
```

### Example:

```
=== Stock Portfolio Tracker ===
Available stocks: AAPL, TSLA, MSFT, AMZN, GOOGL

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 5
Enter stock symbol (or 'done' to finish): TSLA
Enter quantity of TSLA: 3
Enter stock symbol (or 'done' to finish): done
```

**Output:**

```
=== Portfolio Summary ===
AAPL: 5 shares -> $900
TSLA: 3 shares -> $750

Total Investment Value: $1650
```

---

## 💾 Saving Results

* You can choose to save your portfolio summary as:

  * `portfolio.txt`
  * `portfolio.csv`

---

## 📌 Future Improvements

* Fetch **live stock prices** from Yahoo Finance / Alpha Vantage API.
* Add a **Streamlit web app** version.
* Support multiple portfolios.

---

## 👩‍💻 Author

**Rabia Nadeem**
GitHub: [rabianadeem1](https://github.com/rabianadeem1)

