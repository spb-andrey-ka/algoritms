"""
Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе. Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.
"""

from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    if len(first_number) > len(second_number):
        first_number, second_number = second_number, first_number

    first_number = '0' * (
            len(second_number) - len(first_number)) + first_number
    add_one = 0
    result = ''
    for i in range(len(second_number) - 1, -1, -1):
        s = int(first_number[i]) + int(second_number[i]) + add_one
        add_one, s = divmod(s, 2)
        result += str(s)
    if add_one == 1:
        result += '1'
    return result[::-1]

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
