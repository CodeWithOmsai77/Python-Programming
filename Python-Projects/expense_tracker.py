"""A small expense tracker that saves records in a JSON file."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return [
                item for item in data
                if isinstance(item, dict)
                and isinstance(item.get("description"), str)
                and isinstance(item.get("amount"), (int, float))
                and item["amount"] >= 0
            ]
        print("Expense data has an unexpected format; starting with an empty list.")
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not load saved expenses: {error}")
    return []


def save_expenses(expenses):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=2)
        return True
    except OSError as error:
        print(f"Could not save expenses: {error}")
        return False


def read_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount > 0:
                return amount
            print("Amount must be greater than zero.")
        except ValueError:
            print("Enter a valid number.")


def list_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Expenses ---")
    for number, item in enumerate(expenses, start=1):
        print(f"{number:>2}. {item['description']:<24} {item['amount']:>10.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Show summary")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            description = input("Description: ").strip()
            if not description:
                print("Description cannot be empty.")
                continue
            amount = read_amount()
            expenses.append({"description": description, "amount": amount})
            if save_expenses(expenses):
                print("Expense saved.")
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            if not expenses:
                print("No expenses to summarize.")
            else:
                total = sum(item["amount"] for item in expenses)
                largest = max(expenses, key=lambda item: item["amount"])
                print(f"Number of expenses: {len(expenses)}")
                print(f"Total: {total:.2f}")
                print(f"Average: {total / len(expenses):.2f}")
                print(
                    f"Largest: {largest['description']} "
                    f"({largest['amount']:.2f})"
                )
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
