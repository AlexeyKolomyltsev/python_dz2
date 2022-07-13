# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def print_array(array):  # печать массива
    for i in range(len(array)):
        if i == 0:
            print(end="{")
            print(f"{i+1}: {array[i]}", end=", ")
        elif 0 < i < len(array)-1:
            print(f"{i+1}: {array[i]}", end=", ")
        else:
            print(f"{i+1}: {array[i]}", end="}")


def posledovatelnost(num):  # заполнение массива
    array = [2]
    for i in range(1, num):
        array.append(array[i-1] + (round((1+1/(i+1)) ** (i+1), 2)))
    return array


num_p = int(input("Введите количество элементов последовательности (1+1/n)^n ="))
print_array(posledovatelnost(num_p))
