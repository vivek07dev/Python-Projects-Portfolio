import math

def check_amount(amount):
    if amount > 0:
        return True
    else:
        return False

def total_amount(expenses):
    total = 0
    for e in expenses:
        total = total + e[4]
    total = round(total, 2)
    return total