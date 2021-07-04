from collections import *

'''
     Пользователь вводит данные о количестве предприятий,
    их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
    Программа должна определить среднюю прибыль (за год для всех предприятий) 
    и вывести наименования предприятий, чья прибыль выше среднего и отдельно 
    вывести наименования предприятий,чья прибыль ниже среднего.
'''

company = {}
txt = 'Введите компанию и прибыль за 4 квартала через пробел: \n'

while (inp := input(txt)) != 'q':
    print('q для выхода')
    inp = inp.split(' ')
    print(inp)
    inp = list(inp)
    n, amount = inp[0], (int(inp[1]) + int(inp[2]) + int(inp[3]) + int(inp[4]))
    company[n] = amount
print(company)

mean_grade = sum(company.values()) / len(company)

for key in company.keys():
    if company[key] > mean_grade:
        print(key, 'прибыль выше среднего')
print('предприятий,чья прибыль ниже среднего:')
for key in company.keys():
    if company[key] < mean_grade:
        print(key, 'прибыль ниже среднего')

print('-------- Task 2 ----------')

"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры числа. 
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


def m_dex(string):
    dex = 0
    num = deque(string)
    # num = list(string)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def m_hex(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
         '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

num_1 = m_dex(input('Введите первое число в шестнадцатиричном формате: ').upper())
num_2 = m_dex(input('Введите второе число в шестнадцатиричном формате: ').upper())

print(f'Сумма чисел: {m_hex(num_1 + num_2)}')
print(f'Произведение чисел: {m_hex(num_1 * num_2)}')
