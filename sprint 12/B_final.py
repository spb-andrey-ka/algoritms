"""
B. Калькулятор
"""
# ID -- 85367249

import operator


operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
    }


class Stack:
    """Класс стэк."""
    
    def __init__(self):
        self.items = []

    def push(self, item: int) -> None:
        """Добавить элемент на вершину стэка."""
        self.items.append(item)

    def pop(self) -> int:
        """Убрать элемент с вершины стэка."""
        return self.items.pop()


def main():
    input_expression = input().split()
    stack = Stack()
    for i in input_expression:
        if i in operators:
            number_2 = stack.pop()
            number_1 = stack.pop()
            stack.push(operators[i](number_1, number_2))
        else:
            stack.push(int(i))
    print(stack.pop())


if __name__ == '__main__':
    main()
