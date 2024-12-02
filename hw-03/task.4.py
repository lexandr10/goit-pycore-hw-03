

from datetime import datetime,  timedelta


def get_upcoming_birthdays(users):
    result = []
    date_now = datetime.today().date()
    next_week = date_now + timedelta(days=7)
    for user in users:
        
        birthday = datetime.strptime(user["birthday"], '%Y.%m.%d').date()
        birthday_this_year = birthday.replace(year=date_now.year)
        if birthday_this_year < date_now: 
            birthday_this_year = birthday_this_year.replace(year=date_now.year + 1)
        if date_now <= birthday_this_year <= next_week:
            if birthday_this_year.weekday() in (5, 6): 
                days_to_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=days_to_monday)
            else:
                congratulation_date = birthday_this_year
            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })


        
        
    return result

users = [
    {"name": "John Doe", "birthday": "1985.12.02"},
    {"name": "Jane Smith", "birthday": "1990.12.01"},
    {"name": "Emily Davis", "birthday": "1995.12.03"},
    {"name": "Michael Brown", "birthday": "2000.12.06"},
    {"name": "Chris Green", "birthday": "1987.12.07"},
]

birthdays = get_upcoming_birthdays(users)
for b in birthdays:
    print(b)