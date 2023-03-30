# B. Ловкость рук
# ID успешного решения - 84839306

from typing import List, Tuple


MATRIX_SIZE = 4
BOYS = 2


def read_input() -> Tuple[int, List[str]]:
    """Считывает ввод в переменные."""
    boymaxkey = int(input())
    matrix = [str(input()) for i in range(MATRIX_SIZE)]
    return boymaxkey, matrix


def trainer(boymaxkey: int, matrix: List[str]) -> int:
    """Проводим подсчёт результатов игры."""
    numbers = {a: 0 for a in range(1, 10)}
    scores = 0
    for i in range(MATRIX_SIZE):
        for k in matrix[i]:
            if k == '.':
                continue
            numbers[int(k)] += 1
    for i in numbers.values():
        if 0 < i <= 2 * boymaxkey:
            scores += 1
    return scores


if __name__ == '__main__':
    boymaxkey, matrix = read_input()
    print(trainer(boymaxkey, matrix))
