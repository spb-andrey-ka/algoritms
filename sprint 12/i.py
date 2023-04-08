"""
I. Ограниченная очередь

Астрологи объявили день очередей ограниченного размера.
Тимофею нужно написать класс MyQueueSized, который принимает параметр max_size,
означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой очереди.
Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». При вызове операций pop()
или peek() для пустой очереди нужно вывести «None».
Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.
"""
# ID -- 85303576

class MyQueueSized:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_n = size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
  
    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')
    
    def pop(self):
        if self.is_empty():
            print('None')
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            print(x)


def main():
    counter_commands = int(input())
    size = int(input())
    queue = MyQueueSized(size)

    for i in range(counter_commands):
        input_text = input().split()
        if input_text[0] == 'peek':
            print(queue.queue[queue.head])
        elif input_text[0] == 'pop':
            queue.pop()
        elif input_text[0] == 'push':
            queue.push(int(input_text[1]))
        elif input_text[0] == 'size':
            print(queue.size)

if __name__ == '__main__':
    main()