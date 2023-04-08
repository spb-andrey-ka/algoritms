"""
G. Стек - MaxEffective

Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None. При этом push(x) и pop()
также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 100000.
Далее идут команды по одной в строке. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None»,
для команды pop — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой,
для команды get_max() напечатайте «None». Если происходит удаление из
пустого стека — напечатайте «error».
"""
# ID --85223639

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.items_max = []

    def size(self):
        return len(self.items)

    def push(self, item):
        if self.size():
            self.items.append(item)
            if item >= self.items_max[-1]:
                self.items_max.append(item)
        else:
            self.items.append(item)
            self.items_max.append(item)

    def pop(self):  
        if self.size():
            out = self.items.pop()
            if self.items_max[-1] == out:
                self.items_max.pop()
        else:
            print('error')

    def get_max(self):
        if self.size():
            print(self.items_max[-1])
        else:
            print('None')


def main():
    x = int(input())
    stack = StackMaxEffective()

    for i in range(x):
        input_text = input().split()
        if input_text[0] == 'get_max':
            stack.get_max()
        elif input_text[0] == 'pop':
            stack.pop()
        elif input_text[0] == 'push':
            stack.push(int(input_text[1]))


if __name__ == '__main__':
    main()
