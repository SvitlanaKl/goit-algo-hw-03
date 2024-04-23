# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел
# для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі
# повинні бути унікальні.

# Вимоги до завдання:

# Параметри функції:
# min - мінімальне можливе число у наборі (не менше 1).
# max - максимальне можливе число у наборі (не більше 1000).
# quantity - кількість чисел, які потрібно вибрати (значення між min і max).
# Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
# Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися.
# Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.


import random
# # Задаємо параметри діапазону та кількості номерів лотереї
# min = int(input("Please input the minimum number in range (any number above 1): "))
# max = int(input("Please input the maximum number in range (any number between 1 and 1000: "))
# quantity = int(input("How many numbers are there in the lotery? "))

# Формуємо функцію

def get_numbers_ticket(min: int, max: int, quantity: int): 
    if min <1 or max > 1000:
        raise ValueError("Значення повинні бути цілими числами від 1 до 1000 включно.")
    if quantity <1 or quantity > (max-min+1):
        raise ValueError("Кількість виграшних номерів не може перевищувати кількісьб номерів у заданому діапазоні значень.")
    
    count = 0                                           # Визначаємо нульову кількість обраних номерів до старту лотереї
    lottery_numbers = []                                # Задаємо результатам формат списку
    
    while len(lottery_numbers) != quantity:
        step_number = random.randint(min, max)
        if step_number not in lottery_numbers:          # Перевірка чи число вже є у списку
            lottery_numbers.append(step_number)         # Додаємо випадковий номер до списку результатів
               
    sorted_lottery_numbers = sorted(lottery_numbers)
    return sorted_lottery_numbers

lottery_numbers = get_numbers_ticket(1, 2, 2)
print("Ваші лотерейні числа:", lottery_numbers)
    



    




