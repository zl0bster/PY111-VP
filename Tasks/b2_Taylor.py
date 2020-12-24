"""
Taylor series
"""
from typing import Union
from math import factorial, exp
from itertools import count

ACCURACY = 0.0001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    def item(x, n):
        return pow(x, n) / factorial(n)

    sum = 1
    for i in count(1):
        value = item(x, i)
        print(value)
        sum += value
        print(sum)
        if abs(value) <= ACCURACY:
            return sum


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
    print(ex(1.55433))
    print(exp(1.55433))
