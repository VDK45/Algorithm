import random

print('\n----------------------- Task 1 Сортировка пузырька --------------------------\n')
'''1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''

numbers = [random.randint(-100, 100) for _ in range(10)]
print('Исходный массив:\n', numbers)


def buble_sort(n):
    x = len(n)
    while x > 1:
        x -= 1
        for i in range(x):
            if n[i] < n[i + 1]:
                n[i], n[i + 1] = n[i + 1], n[i]
    return n


buble_sort(numbers)
print('Отсортированный массив по убыванию:\n', buble_sort(numbers))
print("---- Version 2 ----")
numbers = [random.randint(-100, 100) for _ in range(10)]


def bubble_reverse(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


print('Исходный массив:\n', numbers)
print('Отсортированный массив по убыванию:\n', bubble_reverse(numbers))

print('\n--------------- Task 2: Сортировка слиянием -----------------\n')
'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
'''


def merge_two_list(a, b):  # Слияние (a и b)
    c = []  # Общий массив c из A и B
    i = j = 0  # счётчики i(a) =  j(b) = 0
    while i < len(a) and j < len(b):  # Контроль длины массива
        if a[i] <= b[j]:  # Если элемент в массиве A меньше
            c.append(a[i])  # Добавляем из массива A в массив C
            i += 1  # Повышаем счётчик i на 1
        else:  # Иначе
            c.append(b[j])  # Добавляем элемент из массива B
            j += 1  # Повышаем счётчик j на 1

    if i < len(a):  # Если в массиве A ещё отались элементы
        c += a[i:]  # Добавить остаток из А в С
    if j < len(b):  # Если в массиве B ещё отались элементы
        c += b[j:]  # Добавить остаток из  В в С
    return c


def merge_sort(s):  # Сортировка слиянием
    if len(s) == 1:  # Если массив из 1 элемента
        return s  # Вернуть масив
    middle = len(s) // 2  # Делит масив на 2 части
    left = merge_sort(s[:middle])  # Левая часть
    right = merge_sort(s[middle:])  # Правая часть
    return merge_two_list(left, right)  # Исользовать слиянием


numbers = [random.randint(0, 50) for _ in range(10)]
print(numbers)
print(merge_sort(numbers))

print('\n--------------- Task 3: Найти медиану -----------------\n')

'''
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
 Найдите в массиве медиану. 
 Медианой называется элемент ряда, делящий его на две равные части: 
 в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. 
Но если это слишком сложно, то используйте метод сортировки, 
который не рассматривался на уроках.
'''

n = int(input("Enter number: "))
a = 2 * n + 1  # Длина массива
lst = [random.randint(0, 100) for _ in range(a)]

lst_check = []
for i in lst:
    lst_check.append(i)  # COPY FOR CHECK

print(f"Длина массива {n} * 2 + 1 = {a} элементов \nlist = {lst} ")

m = len(lst) // 2  # Длина массива делить на 2
n = 0  # Счётик цикла
while n < m:  # Проходить по массиву m раз
    for i in range(0, len(lst) - 1):  # Проходить по массиву от начала до конца не включая
        if lst[i] < lst[i + 1]:  # если предыдущий меньше следующего
            lst[i], lst[i + 1] = lst[i + 1], lst[i]  # Поменять местами
    lst.remove(lst[-1])  # Получится в конце списка самое большое число и его нужно удалить

    k = 0  # Счётик внутреннего цикла
    for j in range(0, len(lst) - 1):  # Проходить по массиву от конца до начала
        k += -1  # Счётик +1
        if lst[k] > lst[k - 1]:  # если предыдущий больше следующего
            lst[k], lst[k - 1] = lst[k - 1], lst[k]  # Поменять местами
    lst.remove(lst[0])  # Получится в начале списка самое маленькое число и его нужно удалить
    # И так каждый проход удаляем самое большое число и самое маленькое
    n += 1  # Проходим m раз и останется медиана

str_m = ''.join(str(e) for e in lst)
print(f"Median = {str_m}")

print("------- Check --------")

print('list =', lst_check)
a = sorted(lst_check)
print('Median =', a[len(a) // 2])

print("------- version 2 --------")  # Не мое решение но для ознакомления


def median_without_sort(arr):
    pivot = arr[0]

    less_med_elems = []  # меньше медианного элемента
    greater_med_elems = []  # больше медианного элемента
    left = 0  # левое
    right = 0  # правое

    # считаем за один прогон и плечи медианы
    # и вычисляем диапазон поиска новой медианы
    for i in array:
        if i < pivot:
            left += 1
        elif i > pivot:
            right += 1

        if i in arr:
            if i < pivot:
                less_med_elems.append(i)
            elif i > pivot:
                greater_med_elems.append(i)

    if left > right:
        return median_without_sort(less_med_elems)
    elif left < right:
        return median_without_sort(greater_med_elems)

    return pivot


n = int(input("Введите положительное целое: "))
m = 2 * n + 1
print(f"Количество элементов m = 2 * {n} + 1 = {m}")

# сделаем список из 2 &* m + 1 не повторяющихся элементов
max_val = pow(m, 2)
array = []
while len(array) < m:
    x = random.randint(0, max_val)
    if x not in array:
        array.append(x)

print(f"Медиана для массива {array} из {m} элементов = {median_without_sort(array)} без сортировки")

print("------- Check --------")

print('list =', array)
a = sorted(array)
print('Median =', a[len(a) // 2])
