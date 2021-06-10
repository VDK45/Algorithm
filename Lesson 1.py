#pylint:disable=E0001
#1. Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

print("-------- task 1 ---------")
try:
	x = int(input('Введите трехзначное число: '))
except ValueError:
	print('Non-numeric input detected.')
	x = 0
d1 = x % 10
x = x // 10
d2 = x % 10
x = x // 10
print(f"{x} + {d2} + {d1} = {d1 + d2 + x}")

#2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

print("-------- task 2 -------")
a = 5
b = 6
print(f"{a} = {bin(a)}") 
print(f"{b} = {bin(b)}") 
print('Логическая побитовая операция И: ')
print(f"{a} & {b} = {a&b} ({bin(a&b)})")
print('Логическая побитовая операция ИЛИ: ')
print(f"{a} | {b} = {a|b} ({bin(a|b)})")
print('Логическая побитовая операция (Исключающее ИЛИ): ')
print(f"{a} ^ {b} = {a^b} ({bin(a^b)})")
print('Побитовый сдвиг вправо два знака: ')
print(f"{b} << 2 = {b<<2} ({bin(b<<2)})")
print('Побитовый сдвиг влево два знака: ')
print(f"{b} >> 2 = {b>>2} ({bin(b>>2)})")



#3. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

print("------- task 3 --------")
print("Координаты точки A(x1;y1):")
try:
	x1 = float(input("x1 = "))
	y1 = float(input("y1 = "))
except ValueError:
	print('Non-numeric input detected. \n x1 = 0 \n y1 = 0')
	x1 = 0
	y1 = 0
print("Координаты точки B(x2;y2):")
try:
	x2 = float(input("x2 = "))
	y2 = float(input("y2 = "))
except ValueError:
	print('Non-numeric input detected. \n x2 = 0 \n y2 = 0')
	x2 = 0
	y2 = 0
print("Координаты точки B(x2;y2):")
print("Уравнение прямой, проходящей через эти точки:")
try:
	k = (y1 - y2) / (x1 - x2)
except ZeroDivisionError:
	print('Zero division error  \n k = 0')
	k = 0
b = y2 - k*x2
print(" y = %.2f * x + %.2f" % (k, b))


#4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

print("------- task 4 -------")
from random import random

try:
	m1 = int(input("Целое число от: "))
	m2 = int(input("Целое число до: "))
except ValueError:
	print('Non-numeric input detected.' )
	m1 = 0
	m2 = 1
n = int(random() * (m2-m1+1)) + m1
print(n)
try:
	m1 = float(input("Вещественное число от: "))
	m2 = float(input("Вещественное число до: "))
except ValueError:
	print('Non-numeric input detected. ')
	m1 = 0
	m2 = 1
n = random() * (m2-m1) + m1
print(round(n,3))
 
m1 = ord(input("Случайный символ от: "))
m2 = ord(input("Случайный символ до: "))
n = int(random() * (m2-m1+1)) + m1
print(f"Случайный символ:{chr(n)}")


#5. Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят и сколько между ними находится букв.

print("------- task 5 -------")
a = ord(input('Первая буква: '))
b = ord(input('Вторая буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f"Позиции {a} и {b}")
print(f'Между буквами {abs(a-b)-1} символов:')


#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


print("------- task 6 -------")
try:
	n = int(input('Номер буквы в алфавите: '))
except ValueError:
	print('Non-numeric input detected. Value = 1')
	n = 1
n = ord('a') + n - 1
print(f"Это буква {chr(n)}")



#7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует,
# то определить, является ли он разносторонним, равнобедренным или равносторонним.

print("------- task 7 -------")

try:
	a = int(input("Сторона a = "))
	b = int(input("Сторона b = "))
	c = int(input("Сторона c = "))
except ValueError:
	print('Non-numeric input detected.') 
	a = 0
	b = 0
	c = 0
if a + b <= c or a + c <= b or b + c <= a:
    print("Не бывает такой треугольник")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")


#8. Определить, является ли год, который ввел пользователем,
# високосным или невисокосным.


print("------- task 8 -------")
try:
	y = int(input("Введите год: "))
except ValueError:
	print('Non-numeric input detected. Value = 2000') 
	y = 2000

if y % 4 != 0:
    print("Обычный год")
elif y % 100 == 0:
    if y % 400 == 0:
        print("Високосный год")
    else:
        print("Обычный год")
else:
    print("Високосный год")


#9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).


print("------- task 9 -------")
x = input('Введите три числа через пробел: ').split()
try:
	a = int(x[0])
	b = int(x[1])
	c = int(x[2])
except (ValueError, IndexError, NameError) as er:
	print(er) 
	a = 0
	b = 0
	c = 0
 
if b < a < c or c < a < b:
    print('Среднее число:', a)
elif a < b < c or c < b < a:
    print('Среднее число:', b)
else:
    print('Среднее число:', c)
