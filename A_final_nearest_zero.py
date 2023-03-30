# A. Ближайший ноль
# ID успешного решения - 84841407

from typing import List, Tuple


def read_input() -> Tuple[List[int], int]:
    """Считывает ввод в переменные."""
    number_plots = int(input())
    houses = list(map(int, input().strip().split()))
    return houses, number_plots


def get_distance(houses: List[str], number_plots: int) -> List[int]:
    """Высчитывает дистанцию каждого из участков до ближайшего нулевого участка."""
    distanse = [number_plots] * number_plots
    zero = [i for i in range(number_plots) if houses[i] == 0]
    first_zero = zero[0]
    last_zero = zero[-1]

    for i in range(first_zero, number_plots):
        if houses[i] != 0:
            distanse[i] = distanse[i - 1] + 1
        else:
            distanse[i] = 0
    for i in range(last_zero, first_zero, -1):
        if houses[i] != 0:
            distanse[i] = min(distanse[i], distanse[i + 1] + 1)
        else:
            distanse[i] = 0
    for i in range(first_zero - 1, -1, -1):
        distanse[i] = distanse[i + 1] + 1
    return distanse


if __name__ == '__main__':
    houses, number_plots = read_input()
    print(" ".join(map(str, get_distance(houses, number_plots))))
