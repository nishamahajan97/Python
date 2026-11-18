import json

FILE = "expenses.json"

def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f)

def add_expense(expenses):
    title = input("Kharcha kis cheez ka hai? ")
    amount = float(input("Kitna paisa? "))
    expenses.append({"title": title, "amount": amount})
    save_expenses(expenses)
    print("Kharcha add ho gaya!")

def show_expenses(expenses):
    if len(expenses) == 0:
        print("Abhi koi kharcha nahi hai.")
        return
    for i, e in enumerate(expenses, start=1):
        print(i, e["title"], "-", e["amount"])

def total_expense(expenses):
    total = 0
    for e in expenses:
        total += e["amount"]
    print("Total kharcha:", total)

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add  2. Show  3. Total  4. Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Galat choice")

main()