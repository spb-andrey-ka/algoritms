# A. Ближайший ноль
# ID успешного решения - 

from typing import List, Tuple

def read_input() -> Tuple[List[int], int]:
    """Считывает ввод в переменные."""
    n = int(input())
    houses = list(map(int, input().strip().split()))
    return houses, n


def main():
    houses, n = read_input()
    print(" ".join(map(str, get_distance(houses, n))))


if __name__ == '__main__':
    main()