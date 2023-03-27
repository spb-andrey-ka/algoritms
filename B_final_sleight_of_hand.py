# B. Ловкость рук
# ID успешного решения - 

from typing import List, Tuple


MATRIX_SIZE = 4
BOYS = 2


def read_input() -> Tuple[int, List[str]]:
    number = int(input())
    matrix = [str(input()) for i in range(MATRIX_SIZE)]
    return number, matrix

