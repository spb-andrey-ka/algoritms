"""
C. Соседи

Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.

Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.

Формат ввода
В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят 1000. В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000. В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.
"""

from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int, n: int, m: int) -> List[int]:
    neighbours = []
    for i in range(row-1, row+2, 2):
        if i < 0 or i > n-1:
            continue
        else:
            neighbours.append(matrix[i][col])
    for i in range(col-1, col+2, 2):
        if i < 0 or i > m-1:
            continue
        else:
            neighbours.append(matrix[row][i])
    return sorted(neighbours)

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col, n, m

matrix, row, col, n, m = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col, n, m))))
