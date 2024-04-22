# вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати.
# Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        try:
            birthdate = datetime.strptime(user["birthday"], '%Y.%m.%d').date()
        except ValueError:
            raise ValueError('Please enter date in format "%Y.%m.%d"')
    
    if birthdate < today: #якщо в цьому році вже минув день народження, змінити в даті рік на наступний
        birthdate = birthdate.replace(year=today.year+1)
    days_to_birthday = (birthdate-today).days

    if days_to_birthday <=7:
        if birthdate.weekday() == 5:
            birthdate += timedelta(days=2)
        elif birthdate.weekday() == 6:
            birthdate += timedelta(days=1)
        else:
            birthdate
    
    upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthdate.strftime("%Y.%m.%d")})
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.04.24"},
    {"name": "Jane Smith", "birthday": "1990.04.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)