from typing import Sequence, Optional, Callable
import itertools
import math


def cri_max(a, b):
    return a > b


def window_search(window_size: int, arr: Sequence, criteria: Callable) -> Optional[int]:
    """
    Returns the position of window center in array where criteria is satisfied

    :param window_size: the dimension of window to analize
    :param arr: array where element is to be found
    :return: Index of element where criteria is satisfied
    """

    def count_weights(n: int) -> Sequence[float]:
        mid = n // 2
        weights: float = [x for x in itertools.repeat(0, n)]
        weights[mid] = 1.0
        for x in range(1, mid):
            weights[mid - x] = (mid - x) / mid
            weights[mid + x] = (mid - x) / mid
        # print(n, mid, weights)
        return weights

    def count_window_value(index: int) -> float:
        """calculates sum of all arr values in window range"""
        # todo check weight calculation
        winLt = index - lt
        winRt = index + rt
        weigth = 0
        nw = 0
        if winLt < 0:
            result = math.fsum(arr[winLt:])
            result += math.fsum(arr[:winRt])
            print(winLt, winRt)
            for j in range(field_len + winLt, field_len):
                weigth += arr[j] * weights[nw]
                nw += 1
            for j in range(0, rt):
                weigth += arr[j] * weights[nw]
                nw += 1
        elif winRt > field_len:
            result = math.fsum(arr[winLt:])
            result += math.fsum(arr[:winRt - field_len])
            print(winLt, winRt)
            for j in range(field_len + winLt, field_len):
                weigth += arr[j] * weights[nw]
                nw += 1
            for j in range(0, rt):
                weigth += arr[j] * weights[nw]
                nw += 1
        else:
            result = math.fsum(arr[winLt:winRt])
            for j in range(lt, rt):
                # print(j, arr[j])
                weigth += arr[j] * weights[nw]
                nw += 1
        return result, weigth

    win_val = []
    wei_val = []
    weights = count_weights(window_size)
    field_len = len(arr)
    if window_size >= field_len:
        return None
    lt = window_size // 2
    rt = window_size - lt
    for i in range(0, field_len):
        result = count_window_value(i)
        win_val.append(result[0])
        wei_val.append(result[1])
    print(max(win_val))
    for i in range(0, field_len - 1):
        print(arr[i], win_val[i], wei_val[i])
    # print(win_val)


if __name__ == '__main__':
    data = [i for i in itertools.repeat(1, 100)]
    pos = len(data) // 3 - 5
    print(f'position = {pos}')
    data[pos] += 10
    data[pos - 2] += 5
    data[pos + 2] += 5
    # print(data)
    print(window_search(window_size=20, arr=data, criteria=cri_max))
