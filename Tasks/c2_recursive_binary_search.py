from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if len(arr) < 2:
        if arr[0] != elem:
            return None
    lt = 0
    rt = len(arr) - 1
    if arr[lt] == elem:
        return lt
    if arr[rt] == elem:
        while arr[rt - 1] == elem:
            rt -= 1
        return rt
    mid = (lt + rt + 1) // 2
    if arr[mid] == elem:
        while arr[mid - 1] == elem:
            mid -= 1
        return mid
    if elem > arr[mid]:
        lt = mid + 1
    else:
        rt = mid - 1
    result = binary_search(elem, arr[lt:rt + 1])
    if result == None:
        return None
    return result + lt


if __name__ == '__main__':
    arr = [i for i in range(100)] + [101]
    print(binary_search(2, [1, 2, 2, 2]))
    print(binary_search(5, arr))
    print(binary_search(54, arr))
    print(binary_search(-1, arr))
