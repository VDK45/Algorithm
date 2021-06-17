print('--------- Task 1 ---------')
'''
    . В диапазоне натуральных чисел от 2 до 99 определить,
    сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

a = [2, 3, 4, 5, 6, 7, 8, 9]
b = range(2, 99 + 1)
c = [0] * 8
for i in b:
    for j in range(2, len(a) + 2):
        if i % j == 0:
            c[j - 2] += 1
x = 0
while x < len(c):
    print(f' Кратных {x + 2} - {c[x]}')
    x += 1

print('--------- Task 2 ---------')
'''
    Во втором массиве сохранить индексы четных элементов первого массива. 
    Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то 
    во второй массив надо заполнить значениями 1, 4, 5, 6 
    (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. 
    именно в этих позициях первого массива стоят четные числа.
'''

from random import randint

N = 15
a = [randint(1, 100) for i in range(N)]
even = []
idx = 0
print(a)
for i in a:
    idx += 1
    if i % 2 == 0:
        even.append(idx - 1)
print('Индексы четных элементов: ', even)

N = 15
arr = [randint(1, 100) for i in range(N)]
even = []
for i in range(N):
    arr[i] = randint(10, 19)
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)

print('--------- Task 3 ---------')
'''
    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint

N = 8
a = [randint(1, 100) for i in range(N)]
print(a)
min = 100
max = 0
idx = 0
idx_min = 0
idx_max = 0
for i in range(N):
    idx += 1
    if a[i] < min:
        idx_min = idx - 1
        min = a[i]
    elif a[i] > max:
        idx_max = idx - 1
        max = a[i]

print(f'Минимальное {min} index {idx_min} \nМаксимальное {max} index {idx_max}')

a[idx_min], a[idx_max] = a[idx_max], a[idx_min]
print(a)

print('--------- Task 4 ---------')
'''
    Определить, какое число в массиве встречается чаще всего.
'''

from random import randint

N = 15
a = [randint(1, 20) for i in range(N)]
print(a)
num = a[0]
max_frq = 1
for i in range(len(a) - 1):
    frq = 1
    for k in range(i + 1, len(a)):
        if a[i] == a[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = a[i]
if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')

print('--------- Task 5 ---------')
from random import randint

'''
    В массиве найти максимальный отрицательный элемент. 
    Вывести на экран его значение и позицию в массиве.
'''
N = 10
a = [randint(-20, 20) for i in range(N)]
print(a)
num = a[0]
max_neg = -1000
idx = 0
pos = 0
for i in a:
    pos += 1
    if i > max_neg and i < 0:
        max_neg = i
        idx = pos - 1

print(f'Максимальный отрицательный элемент с индексом: {idx} Значение: {max_neg}')

print('--------- Task 6 ---------')
from random import randint

'''
    В одномерном массиве найти сумму элементов, 
    находящихся между минимальным и максимальным элементами. 
    Сами минимальный и максимальный элементы в сумму не включать.
'''

N = 8
a = [randint(1, 100) for i in range(N)]
print(a)
min = 100
max = 0
idx = 0
idx_min = 0
idx_max = 0
for i in range(N):
    idx += 1
    if a[i] < min:
        idx_min = idx - 1
        min = a[i]
    elif a[i] > max:
        idx_max = idx - 1
        max = a[i]

print(f'Минимальное {min} index {idx_min} \nМаксимальное {max} index {idx_max}')

if idx_max < idx_min:
    idx_max, idx_min = idx_min, idx_max

suma = 0
for i in range(idx_min + 1, idx_max):
    suma += a[i]
print(f'Сума между {a[idx_min]} и {a[idx_max]} = {suma}')

print('--------- Task 7 ---------')
"""
	 В одномерном массиве целых чисел определить два наименьших элемента. 
	 Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
from random import randint

m1, m2 = 20, 20

lst = [randint(-10, 10) for i in range(20)]

print(lst)
idx = -1
for i in lst:
    idx += 1
    if i < m1:
        m1 = i
        m_idx = idx

print(m_idx)  # Индекс минимального числа
del lst[m_idx]  # Удалить мин-ое число

print(lst)

for j in lst:
    if j < m2:
        m2 = j

print(m1, m2)

print('--------- Task 8 ---------')
'''
	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
	Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
	В конце следует вывести полученную матрицу.
'''

N = 4  # Количество строк
st = []  # Строка
for i in range(N):
    rd = []  # Ряд
    suma = 0
    nums = input('Введите 4 числа через пробел: ').split()
    for j in nums:
        suma += int(j)  # Сума чисел в nums
        rd.append(int(j))  # Добавлять значение в ряд
    rd.append(suma)  # Добавить суму в ряд
    st.append(rd)
print('\n'.join('\t'.join(str(elem) for elem in row) for row in st))

print('--------- Task 9 ---------')
"""
	Найти максимальный элемент среди минимальных элементов столбцов матрицы
"""
n = 4
st = []

for i in range(n):
    rd = []
    numbs = input("Введите числа через пробел: ").split()
    for j in numbs:
        rd.append(int(j))
    st.append(rd)
print('\n'.join('\t'.join(str(elem) for elem in row) for row in st))

mx = -1
for j in range(len(numbs)):
    mn = 10000
    for i in range(n):
        if st[i][j] < mn:
            mn = st[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
