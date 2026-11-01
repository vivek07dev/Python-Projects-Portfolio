
print("===== STUDENT MONTHLY BUDGET ANALYZER =====")


name = input("Enter student name: ")

income = float(input("Enter monthly income: Rs. "))

food = float(input("Enter food expenses: Rs. "))

travel = float(input("Enter travel expenses: Rs. "))

study = float(input("Enter study material expenses: Rs. "))

mobile = float(input("Enter mobile/internet expenses: Rs. "))

other = float(input("Enter other expenses: Rs. "))


total_expenses = food + travel + study + mobile + other


balance = income - total_expenses


if total_expenses > 0:

    food_percentage = (food / total_expenses) * 100
    travel_percentage = (travel / total_expenses) * 100
    study_percentage = (study / total_expenses) * 100
    mobile_percentage = (mobile / total_expenses) * 100
    other_percentage = (other / total_expenses) * 100

else:

    food_percentage = 0
    travel_percentage = 0
    study_percentage = 0
    mobile_percentage = 0
    other_percentage = 0




if income > 0:

    savings_rate = (balance / income) * 100

else:

    savings_rate = 0




print("\n===== MONTHLY BUDGET REPORT =====")

print("Student Name:", name)

print("Monthly Income: Rs.", format(income, ".2f"))

print("\n----- EXPENSE DETAILS -----")

print("Food: Rs.", format(food, ".2f"))
print("Food Percentage:", format(food_percentage, ".2f"), "%")

print("Travel: Rs.", format(travel, ".2f"))
print("Travel Percentage:", format(travel_percentage, ".2f"), "%")

print("Study Materials: Rs.", format(study, ".2f"))
print("Study Percentage:", format(study_percentage, ".2f"), "%")

print("Mobile/Internet: Rs.", format(mobile, ".2f"))
print("Mobile Percentage:", format(mobile_percentage, ".2f"), "%")

print("Other: Rs.", format(other, ".2f"))
print("Other Percentage:", format(other_percentage, ".2f"), "%")




print("\n----- FINAL SUMMARY -----")

print("Total Expenses: Rs.", format(total_expenses, ".2f"))

print("Remaining Balance: Rs.", format(balance, ".2f"))

print("Savings Rate:", format(savings_rate, ".2f"), "%")



print("\n----- DATA TYPES -----")

print("Name Type:", type(name))

print("Income Type:", type(income))

print("Total Expenses Type:", type(total_expenses))

print("\nThank You!")