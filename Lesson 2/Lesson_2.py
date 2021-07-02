from sys import getsizeof
print('Python 3.9.1 Windows 10 x64')
print('-------- Task 1 --------')
'''
    Написать программу, которая будет складывать, вычитать, умножать 
    или делить два числа. Числа и знак операции вводятся пользователем. 
    После выполнения вычисления программа не должна завершаться, 
    а должна запрашивать новые данные для вычислений. 
    Завершение программы должно выполняться при вводе символа '0' 
    в качестве знака операции. Если пользователь вводит неверный знак 
    (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об 
    ошибке и снова запрашивать знак операции. Также сообщать пользователю 
    о невозможности деления на ноль, если он ввел 0 в качестве делителя.
'''

print('---- Classic ----')
print('Введите по шаблону 44 + 55 / Enter или 0 для выхода')


def math(a, x, b):
    if x == "*":
        return (a * b)
    elif x == "/":
        return (a / b)
    elif x == "+":
        return (a + b)
    elif x == "-":
        return (a - b)


while 1:
    inp = input("Enter: ").split()
    print(inp)
    if inp == ["0"] or inp == []:
        break
    else:
        print('Result = ', math(int(inp[0]), inp[1], int(inp[2])))
        print("Memory use: ", getsizeof(math(int(inp[0]), inp[1], int(inp[2]))))

#  Память использована 28 байт

print("---- Recursion----")

def math(x, y, z):
    try:
        x = int(input("x = "))
        y = int(input("y = "))
    except ValueError as err:
        print("Wrong enter!")
        math(0 ,0 ,0)
    z = input("Zero for exit, Operation: ")
    if z == "0":
        return print("Exit")
    elif y == 0:
        print("Zero division error!")
    elif z == "*":
        print(x * y)
    elif z == "/":
        print(x / y)
    elif z == "+":
        print(x + y)
    elif z == "-":
        print(x - y)
    else:
        print("Wrong enter!")
    math(0, 0, 0)


print("Memory used: ", getsizeof(math(0 ,0 ,0)))
#  Память использована 16 байт
#  Итог рекурсия использует меньше памяти

print('-------- Task 2 --------')
print('Количество четных и нечетных в номере')
'''Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 четные цифры 
(4, 6 и 0) и 2 нечетные (3 и 5).'''
print('---- Classic ----')


def even_odd():
    even = 0
    odd = 0
    try:
        a = int(input('Введите номер: '))
    except ValueError as err:
        print(err)
        print('Ошибка ввода!')
        a = 0
    while a > 0:
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
        a = a // 10
    return print(f'Количество четных:   {even} \nКоличество нечетных: {odd}')


print('Memory used: ', getsizeof(even_odd()))
#  Память использована 16 байт


print("----- Recursion -----")


def count_numb(n, even=0, odd=0):
    if n <= 0:
        print(f"Количество четных:   {even}")
        print(f'Количество нечетных: {odd}')
    else:
        a = n % 10
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_numb(n // 10, even, odd)


try:
    n = int(input("Введите номер: "))
except ValueError as err:
    n = 0
    print(err)

print('Memory used: ', getsizeof(count_numb(n)))
#  Память использована 16 байт
#  Итог одинаково используют память

print('-------- Task 3 --------')
print('Обратное число 1357778890112')
'''Сформировать из введенного числа обратное по 
порядку входящих в него цифр и вывести на экран. 
Например, если введено число 3486, то надо вывести число 6843.'''

print('----- Classic -----')

a = 1357778890112

b = 0
while a > 0:
    b = b * 10 + a % 10
    a = a // 10
print(b)

print('Memory used:', getsizeof(a))
#  Память использована 24 байт

print('---- Recursion ----')
def help():
    a = []

    def rev(x):
        if x > 0:
            a.append(x % 10)
            rev(x // 10)


    rev(1357778890112)

    k = 1
    d = 0
    suma = 0
    for i in range(len(a) - 1, -1, -1):
        d = a[i]
        d = d * k
        k *= 10
        suma += d
    return print(suma)

print('Memory used:', getsizeof(help()))
#  Память использована 16 байт
#  Итог рекурсия использует меньше памяти

print("-------- Task 5 ---------")
"""
	Вывести на экран коды и символы таблицы ASCII, 
    начиная с символа под номером 32 и заканчивая 127-м включительно. 
    Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""
print('---- Classic ----')


def help():
    j = 0
    for i in range(32, 128 + 1):
        print(f'{i}-{chr(i)}', end=' ')
        j += 1
        if j % 10 == 0:
            print('')
    print('\n')


print("Memory used: ", getsizeof(help()), "\n")
#  Память использована 16 байт

print("---- Recursion ----")


def row():
    k = 0

    def ascii(x):
        nonlocal k
        y = 129
        if x < y:
            k += 1
            print(f'{x}-{chr(x)}', end=' ')
            if k % 10 == 0:
                print("")
            return ascii(x + 1)

    ascii(32)


print("\nMemory used: ", getsizeof(row()))
#  Память использована 16 байт
#  Итог одинаково используют память

print('-------- Task 6 --------')
'''В программе генерируется случайное целое число от 0 до 100. 
Пользователь должен его отгадать не более чем за 10 попыток. 
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
 чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.'''
print('----- classic -----')
from random import random
from sys import getsizeof


def help():
    n = int(random() * 101)
    i = 1
    while i <= 10:
        i += 1
        try:
            x = int(input('Отгадайте число от 0 до 100: '))
        except ValueError:
            print('Ввод не номер!')
            continue
        if x == n:
            print(f'Всё верно это {n}')
            break
        elif i >= 11:
            print(f'Вы проиграли это {n}')
            break
        else:
            print(f'Не верно! {i}-ая попытка')
            if n > x:
                print(f'Нужно больше > {x}')
            else:
                print(f'Нужно меньше < {x}')


print('Memory used:', getsizeof(help()))
#  Память использована 16 байт

print('---- Recursion ----')


def create_counter():
    i = 0

    def random_num(r_num):
        nonlocal i
        input_num = int(input('Enter number: '))
        if r_num == input_num:
            return print(f"Ура это точно {r_num}")
        elif input_num > r_num:
            i += 1
            print(f'Нужно меньше < {input_num}')
            print(f'{i}ая попытка')
            if i == 10:
                return print(f'Вы потрачили все 10 попыток! Это номер {r_num}')
            random_num(r_num)

        elif input_num < r_num:
            i += 1
            print(f'Нужно больше > {input_num} ')
            print(f'{i}ая попытка')
            if i == 10:
                return print(f'Вы потрачили все 10 попыток! Это номер {r_num}')
            random_num(r_num)

    n = int(random() * 101)
    random_num(n)
    return random_num


counter = create_counter()

print('Memory used:', getsizeof(counter))
#  Память использована 136 байт
#  Итог классик использует меньше память
print('-------- Task 7 --------')

'''Напишите программу, доказывающую или проверяющую, 
что для множества натуральных чисел выполняется равенство: 
1+2+...+n = n(n+1)/2, где n - любое натуральное число.'''
print('Сумма от 1 до n')
print("---- Classic ----")


def sum_all(d):
    sum_all = 0
    for i in range(0, d + 1):
        sum_all += i
    return print(sum_all)


print("Memory used: ", getsizeof(sum_all(int(input("Enter n number: ")))))
#  Память использована 16 байт

print("---- Recursion ----")


def sum(n):
    if n == 0:
        return 1
    else:
        return (sum(n - 1) + (n))


n = int(input('ENTER: '))
# print(sum(n)-1)
print("Memory used: ", getsizeof(print(sum(n) - 1)))
#  Память использована 16 байт

print("----- Math ----")


def math(n):
    return n * ((n + 1) / 2)


numb = int(input("Enter: "))

print(math(numb))
print("Memory used: ", getsizeof(math(numb)))
#  Память использована 24 байт
#  Итог класика и рекурсия используют память меньше чем math
print('-------- Task 8 --------')
'''
    Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. 
    Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''
print("---- Classic ----")


def count_digital():
    try:
        n = int(input("Сколько будет чисел? "))
        d = int(input("Какую цифру считать? "))
    except ValueError:
        print("Ввели не число.")
        n = 0
        d = 0
    count = 0
    for i in range(1, n + 1):
        m = int(input("Число " + str(i) + ": "))
        while m > 0:
            if m % 10 == d:
                count += 1
            m = m // 10

    return print(f'Было введено {count} цифр {d}')


print('Memory used: ', getsizeof(count_digital()))
#  Память использована 16 байт

print("---- Recursion ----")


def go():
    how_numbs = int(input('Сколько будет чисел? '))
    check_d = int(input('Какую цифру считать?  '))
    count_d = 0
    k = 0
    for i in range(how_numbs):
        k += 1
        numb = int(input(f'Enter number {k}: '))

        def count(d):
            nonlocal count_d
            a = d % 10
            if a == check_d:
                count_d += 1
            if d != 0:
                count(d // 10)

        count(numb)
    return print('Было введено', count_d)


print('Memory used: ', getsizeof(go()))
#  Память использована 16 байт
#  Итог одинаково используют память

print('-------- Task 9 --------')
'''Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
Вывести на экран это число и сумму его цифр.'''
print('Найти наибольшее по сумме цифр')
print('---- Classic ----')


def max_s():
    try:
        n = int(input('Ноль для остановки. Введите число: '))
    except ValueError:
        return print('Ввели не число. Остановка программы')
    max_s = 0
    max_m = 0
    while n != 0:
        m = n
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        if s > max_s:
            max_s = s
            max_m = m
        try:
            n = int(input())
        except ValueError:
            print('Ввели не число. Остановка программы')
            exit(0)

    return print(f'Число {max_m} имеет максимальную сумму цифр: {max_s}')


print('Memory used: ', getsizeof(max_s()))
#  Память использована 16 байт

print('---- Recursion ----')


def help():
    max_sum = 0
    max_number = 0
    while 1:
        number = int(input('Ноль для остановки.Введите число: '))
        if number == 0:
            return print(f'Число {max_number} имеет максимальную сумму цифр: {max_sum}')
        sum = 0

        def sum_num(num):
            nonlocal sum
            sum += num % 10
            if num != 0:
                return sum_num(num // 10)

        sum_num(number)
        print('Сума цифр: ', sum)
        if sum > max_sum:
            max_sum = sum
            max_number = number


print('Memory used: ', getsizeof(help()))
#  Память использована 16 байт
#  Итог одинаково используют память
