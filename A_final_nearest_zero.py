# A. Ближайший ноль
# ID успешного решения - 84899070

from typing import List, Tuple


def read_input() -> Tuple[List[str], int]:
    """Считывает ввод в переменные."""
    number_plots = int(input())
    houses = input().split()
    return houses, number_plots


def get_distance(houses: List[str], number_plots: int) -> List[int]:
    """Высчитывает дистанцию каждого из участков
    до ближайшего нулевого участка."""
    distance = calculate(houses, number_plots)
    r_distance = (calculate(houses[::-1], number_plots))[::-1]
    result = []
    for i in range(number_plots):
        result.append(min(distance[i], r_distance[i]))
    return result


def calculate(houses: List[str], number_plots: int) -> List[int]:
    """подсчет от нуля"""
    distance = []
    zero = None
    for i, value in enumerate(houses):
        if value == '0':
            zero = i
            distance.append(0)
            continue
        if zero is not None:
            distance.append(i - zero)
        else:
            distance.append(number_plots)
    return distance

if __name__ == '__main__':
    houses, number_plots = read_input()
    print(*get_distance(houses, number_plots), sep=' ')
