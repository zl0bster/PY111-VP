from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    lt = 0
    rt = len(arr) - 1
    if arr[lt] == elem:
        return lt
    if arr[rt] == elem:
        while arr[rt - 1] == elem:
            rt -= 1
        return rt
    while rt > lt:
        mid = (lt + rt) // 2
        if arr[mid] == elem:
            while arr[mid - 1] == elem:
                mid -= 1
            return mid
        if elem > arr[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    return None


if __name__ == '__main__':
    print(binary_search(2, [1, 2, 2, 2]))
