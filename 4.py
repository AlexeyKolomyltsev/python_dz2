#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
def fill_array(num):
    array=[]
    for i in range(-num, num+1):
        array.append(i)
    return array
    
    
def multiplex(arr, indices: str):
    i1, i2 = map(int, indices.split(" "))
    print(f"Результат перемножения = {arr[i1]*arr[i2]}")

  
n = int(input("Введите количество элементов N = "))
arr = fill_array(n)
print(arr)

multiplex(arr, input(f"Введите позиции пары чисел от 0 до {n*2} через пробел "))
