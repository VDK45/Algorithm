'''
    1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
    состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
'''

import hashlib

string = input('Введите строку:\n')

sum_substring = set()
0
for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_substring.add(hash_str)

print(f'{len(sum_substring) - 1} различных подстрок в строке {string}')

'''
    2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
'''
import heapq
from collections import *


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code


def main():
    s = input('Enter text: ')
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)


if __name__ == '__main__':
    main()
