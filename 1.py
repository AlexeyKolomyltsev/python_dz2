# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def fun(num):
    count = 0
    for i in num:
        if i.isdigit(): count += int(i)
    return count
num = input("Введите число: ")
print(f"Сумма цифр числа = {fun(num)}")