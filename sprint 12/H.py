"""
H. Скобочная последовательность

Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она довольно популярная.

Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:

пустая строка —– правильная скобочная последовательность;
правильная скобочная последовательность, взятая в скобки одного
типа, –— правильная скобочная последовательность;
правильная скобочная последовательность с приписанной слева или
справа правильной скобочной последовательностью —– тоже правильная.
На вход подаётся последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную
последовательность и возвращает True, если последовательность правильная, а иначе False.

Формат ввода
На вход подаётся одна строка, содержащая скобочную последовательность.
Скобки записаны подряд, без пробелов.

Формат вывода
Выведите «True» или «False».
"""
# ID -- 85299586


def is_correct_bracket_seq(check_string):
    if not len(check_string):
        return True
    if len(check_string) % 2:
        return False
    etalon = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []
    for i in check_string:
        if i in etalon.values():
            stack.append(i)
            continue
        if len(stack) and etalon[i] == stack[-1]:
            stack.pop()
            continue
        return False
    if not len(stack):
        return True
    return False


def main():
    check_string = input()
    print(is_correct_bracket_seq(check_string))


if __name__ == '__main__':
    main()
