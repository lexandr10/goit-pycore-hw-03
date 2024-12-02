
from datetime import datetime 

def get_days_from_today(date):
    try:
       origin_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return ValueError("Invalid format date")
    current_date = datetime.now()
    delta = origin_date - current_date

    return delta.days

print(get_days_from_today("2021-10-09"))