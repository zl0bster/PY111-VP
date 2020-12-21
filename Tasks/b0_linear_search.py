"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    if not arr:
        return -1
    min_val = arr[0]
    min_ind = 0
    for ind, val in enumerate(arr):
        if val < min_val:
            min_val = val
            min_ind = ind
    return min_ind
