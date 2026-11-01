import datetime as dt

def get_month(expenses):
    now = dt.datetime.now()
    current_month = now.month
    result = []
    for e in expenses:
        d = dt.datetime.strptime(e[0], "%Y-%m-%d")
        if d.month == current_month:
            result.append(e)
    return result

def month_name():
    now = dt.datetime.now()
    return now.strftime("%B %Y")