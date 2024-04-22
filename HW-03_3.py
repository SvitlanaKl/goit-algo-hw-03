#Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, 
#залишаючи тільки цифри та символ '+' на початку. 

#Вимоги до завдання:

# Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
# Функція видаляє всі символи, крім цифр та символу '+'.
# Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') та коли номер починається без коду (додається '+38').
# Функція повертає нормалізований телефонний номер у вигляді рядка.


import re
from collections import defaultdict

def normalize_phone(phone_number: str) -> str:
    first_clean = re.sub(r"\D", "", phone_number)
    if len(first_clean) == 10:
        return ["+38"+first_clean]
    elif len(first_clean) == 12:
        return ["+"+first_clean]
    else:
        return print("Уточніть номер телефону.")


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# check commit to github