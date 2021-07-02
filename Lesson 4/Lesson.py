import cProfile  # Нет параллельных
from random import randint

print('---------------------------- Task 1 ---------------------------')
'''
	Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
	Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''

print("-------- Version 1 --------")


def v1():
    a = [randint(1, 100) for i in range(20)]
    print(a)

    m1, m2 = 200, 200

    idx = -1
    while idx < len(a) - 1:
        idx += 1
        if a[idx] < m1:
            m1 = a[idx]
            m_idx = idx

    print('min index for delete:', m_idx)  # Индекс минимального числа
    del a[m_idx]  # Удалить мин-ое число

    for j in a:
        if j < m2:
            m2 = j
    print('m1 = ', m1)
    print('m2 = ', m2)


a = v1()
cProfile.run('v1()')

print("-------- Version 2 -------")


def v2():
    b = [randint(1, 100) for i in range(20)]

    print(b)
    b.sort()
    print(b, 'После сортировки')

    print("m1 =", b[0], "\nm2 =", b[1])


b = v2()

cProfile.run('v2()')

print("-------- Version 3 ---------")


def v3():
    c = [randint(1, 100) for i in range(20)]

    print(c)
    for i in range(len(c)):
        for j in range(len(c)):
            if c[i] >= c[j]:
                c[i], c[j] = c[j], c[i]
    print(c)
    print("m1 =", c[-1])
    print("m2 =", c[-2])


c = v3()

cProfile.run('v3()')

print('Result:')
'''
    Результаты в Пайчарм: 
     Version 1 ncalls = 135 function calls in 0.000 seconds
     Version 2 ncalls = 117 function calls in 0.000 seconds
     Version 3 ncalls = 135 function calls in 0.000 seconds
    Результаты в IDLE Shell: 
     Version 1 ncalls = 888 function calls in 0.016 seconds
     Version 2 ncalls = 868 function calls in 0.028 seconds
     Version 3 ncalls = 784 function calls in 0.022 seconds
'''

print('---------------------------- Task 2 ---------------------------')

'''
    Написать два алгоритма нахождения i-го по счёту простого числа.
    Без использования «Решета Эратосфена»;
    Используя алгоритм «Решето Эратосфена»
    Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
    Результаты анализа сохранить в виде комментариев в файле с кодом.
'''
import timeit
import datetime as dt
import cProfile  # Нет параллельных

print('----- Вариант без (Решето Эратосфена): -----')


def classic(n):
    a = [i for i in range(2, n)]
    i = 2
    for i in a:
        for j in a:
            if j == i:
                continue
            elif j % i == 0:
                a.remove(j)
    return print('A', a)


x = classic(100)

# t_classic = timeit.Timer('classic', 'from Lesson_4 import classic')
# print(t_classic.timeit())

print('----- Решето Эратосфена: -----')


def erat(n):
    a = [i for i in range(n + 1)]

    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    a = set(a)
    a.remove(0)
    a = list(a)
    a.sort()
    return (print('E', a))


y = erat(100)

# t_erat = timeit.Timer('erat', 'from Lesson_4 import erat')
# print(t_erat.timeit())

print('----- Analysis classic: -----')
cProfile.run('classic(100)')
'''
    Pycharm:
    79 function calls in 0.000 seconds 
    IDLE Shell:
    295 function calls in 0.010 seconds
    (хуже с Решето Эратосфена)
'''

print('----- Analysis erat: -----')
cProfile.run('erat(100)')
'''
    Pycharm:
    8 function calls in 0.000 seconds
    IDLE Shell:
    224 function calls in 0.010 seconds
    (Не надо изобретать велосипед, всё уже придумали до нас)
'''
