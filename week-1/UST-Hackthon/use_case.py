import datetime

FILE_NAME = "expenses.txt"

# Add expense
def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")
    date = datetime.date.today()

    file = open(FILE_NAME, "a")
    file.write(f"{date},{amount},{category}\n")
    file.close()

    print("Expense added successfully!")

# Calculate total, average and monthly spend
def expense_summary():
    file = open(FILE_NAME, "r")
    lines = file.readlines()
    file.close()

    total = 0
    count = 0
    monthly_total = 0
    current_month = datetime.date.today().strftime("%Y-%m")

    for line in lines:
        date, amount, category = line.strip().split(",")
        amount = float(amount)

    total += amount
    count += 1

    if date.startswith(current_month):
        monthly_total += amount

    average = total / count

    print("\n📊 Expense Summary")
    print("------------------")
    print(f"Total Expense : ₹{total}")
    print(f"Average Expense : ₹{average:.2f}")
    print(f"This Month : ₹{monthly_total}")

# Menu
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        expense_summary()
    elif choice == "3":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice")