#Реализуйте алгоритм перемешивания списка.
import random
n = int(input("Введите количество элементов в списке "))
array = [random.randint(-100,100) for i in range(n)]
print(array)

def mix(array):
    l = len(array)
    indecs = []     #создаем массив indecs для индексов исходного массива
    new_arr = []
    i = 0
    while(i<l):                    
        j = random.randint(0, l-1) #делаем рандом из диапазона длины исходного массива
        if j not in indecs:
            indecs.append(j)    #если в массиве исходного нет значения индекса исх. массива, добавляем значение в массив
            new_arr.append(array[j]) #в перемешанный массив добавляем соответсвующее значение
            i += 1
    return new_arr
print(mix(array))
