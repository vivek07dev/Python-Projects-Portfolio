import os
import random
import datetime
import expense_utils
from report_utils import get_month
import report_utils as ru
from tabulate import tabulate

expenses = []

print("Expense Tracker")

while True:
    print("\n1. Add expense")
    print("2. Show report")
    print("3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        desc = input("Enter description: ")
        cat = input("Enter category: ")
        amount = float(input("Enter amount: "))

        if expense_utils.check_amount(amount) == False:
            print("Amount must be positive")
            continue

        date_input = input("Enter date (YYYY-MM-DD) or press enter for today: ")
        if date_input == "":
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            date = date_input

        ref = random.randint(100000, 999999)
        ref_id = "EXP-" + str(ref)

        expenses.append([date, ref_id, desc, cat, amount])
        print("Reference ID:", ref_id)

        path = os.path.join(os.getcwd(), "report.txt")
        if os.path.exists(path):
            print("report file exists")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expense")
            continue

        monthly = get_month(expenses)
        
        print("\n----- MONTHLY EXPENSE REPORT -----")
        print(tabulate(monthly, headers=["Date", "Ref ID", "Desc", "Category", "Amount"]))

        total = expense_utils.total_amount(monthly)
        print("\nTotal spending:", total)
        print("Report month:", ru.month_name())

    elif choice == "3":
        break
    else:
        print("Invalid choice")