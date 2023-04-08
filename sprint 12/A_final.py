"""
A. Дек
"""
# ID -- 85367090

from typing import Optional


class StackOverFlow(Exception):
    """Вызывается при добавлении элемента в полный дек."""
    pass


class StackEmpty(Exception):
    """Вызывается при удалении элемента из пустого дек."""
    pass


class Deque:
    """Класс двухсторонней очереди."""

    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 1
        self.size = 0

    def is_empty(self) -> None:
        """Проверка на пустоту."""
        if self.size == 0:
            raise StackEmpty('error')

    def is_full(self) -> None:
        """Проверка на переполненность."""
        if self.size == self.max_n:
            raise StackOverFlow('error')

    def push_front(self, value: str) -> None:
        """Добавить элемент в начало очереди."""
        self.is_full()
        self.queue[self.head] = value
        self.head = (self.head - 1) % self.max_n
        self.size += 1

    def push_back(self, value: str) -> None:
        """Добавить элемент в конец очереди."""
        self.is_full()
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def pop_back(self) -> str:
        """Убрать элемент с конца очереди."""
        self.is_empty()
        self.tail = (self.tail - 1) % self.max_n
        out_element = self.queue[self.tail]
        self.queue[self.tail] = None
        self.size -= 1
        return out_element

    def pop_front(self) -> str:
        """Убрать элемент с начала очереди."""
        self.is_empty()
        self.head = (self.head + 1) % self.max_n
        out_element = self.queue[self.head]
        self.queue[self.head] = None
        self.size -= 1
        return out_element


def run_command(deque) -> Optional[str]:
    """Получает и выполняет команду для переданного дека"""
    command, *arg = input().split()
    try:
        return getattr(deque, command)(*arg)
    except Exception as error:
        return error


def main():
    commands_counter = int(input())
    max_size = int(input())
    deque = Deque(max_size)

    for i in range(commands_counter):
        result = run_command(deque)
        if result:
            print(result)


if __name__ == '__main__':
    main()
