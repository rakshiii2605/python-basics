import pandas as pd
import os

FILENAME = "expenses.csv"

def add_expense(date, category, amount):
    if os.path.exists(FILENAME):
        df = pd.read_csv(FILENAME)
    else:
        df = pd.DataFrame(columns=["Date", "Category", "Amount"])

    new_entry = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    df = pd.concat([df, new_entry], ignore_index=True)

    df.to_csv(FILENAME, index=False)
    print("✅ Expense added successfully!")

def view_expenses():
    if os.path.exists(FILENAME):
        df = pd.read_csv(FILENAME)
        print("\n📊 Expense Records:\n", df)
        print("\n💰 Total Spent:", df["Amount"].sum())
    else:
        print("⚠️ No expenses recorded yet.")

if __name__ == "__main__":
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food, Travel, etc.): ")
            amount = float(input("Enter amount: "))
            add_expense(date, category, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Exiting Expense Tracker.")
            break
        else:
            print("❌ Invalid choice. Try again.")
