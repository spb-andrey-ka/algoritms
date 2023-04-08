"""
F. Стек - Max

Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке. Класс должен поддерживать
операции push(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд,
которое не превосходит 10000. В следующих n строках идут команды.
Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""
# ID -- 85215952

class StackMax:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        if len(self.max) == 0:
            self.max.append(item)
        elif item > self.max[-1]:
            self.max.append(item)
        else:
            self.max.append(self.max[-1])
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        self.max.pop()
        return self.items.pop()

    def get_max(self):
        if self.is_empty():
            return 'None'
        return self.max[-1]

    def is_empty(self):
        return self.items == []


def main():
    n = int(input())

    stack_max = StackMax()
    result = []

    for i in range(n):
        item = input().split()
        if item[0] == 'push':
            stack_max.push(int(item[1]))
        elif item[0] == 'pop':
            if stack_max.pop() == 'error':
                result.append('error')
        elif item[0] == 'get_max':
            result.append(stack_max.get_max())
    for i in result:
        print(i)


if __name__ == '__main__':
    main()