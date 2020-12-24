"""
Taylor series
"""
from typing import Union
from math import factorial
from itertools import count

ACCURACY = 0.0001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)
    return 0


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    def item(n):
        return pow(-1, n - 1) * pow(x, ((n * 2) - 1)) / factorial((2 * n) - 1)

    sum = 0
    for i in count(1):
        value = item(i)
        print(value)
        sum += value
        print(sum)
        if abs(value) <= ACCURACY:
            return sum


if __name__ == '__main__':
    print(sinx(3.14159 / 2))
