# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial_p(num):
    array = [1]
    for i in range(1, num):
        array.append(array[i-1] * (i+1))
    return array
num_p = int(input("Введите количество отображаемых элементов последовательности факториала "))
print(f"Для {num_p} последовательность: {factorial_p(num_p)}")
