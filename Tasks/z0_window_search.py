import itertools
import logging
import math
from typing import Sequence, Optional, Callable


def window_search(window_size: int, arr: Sequence, criterion: Callable) -> Optional[Sequence[int]]:
    """
    Returns the position of window center in array where criteria is satisfied
    window weights are used to localize the position
    Data and structures calculated while function execution are saved in log file

    Алгоритм предназначен для решения задачи поиска типа: как, стоя на лесной поляне, найти направление,
    в котором растет максималльное (минимальное) число деревьев при заданном угле зрения?

    :param window_size: the dimension of window to analize
    :param arr: array where element is to be found
    :param criterion: function to sort window weight values to find maximum or minumum
    :return: Index of element where criteria is satisfied.
            Returns None if window size is bigger than arr length
    """

    def count_weights(n: int) -> Sequence[float]:
        """prepares weights for each window cell"""
        mid = n // 2
        windowWeights = [x for x in itertools.repeat(0.01, n)]
        windowWeights[mid] = 1.0
        for x in range(1, mid):
            # val = (mid - x) / mid # linear mountain
            val = round(math.pow(((mid - x) / mid), 2), 4)  # parabolic mountain
            windowWeights[mid - x] = val
            windowWeights[mid + x] = val
        log.info("window %s mid %s vals %s" % (n, mid, windowWeights))
        return windowWeights

    def count_window_value(index: int) -> Sequence[float]:
        """calculates sum of all arr values in window range and window coefficient circulating on input array """
        winLt = index - lt
        winRt = index + rt
        weigth = 0
        nw = 0
        if winLt < 0:
            result = math.fsum(arr[winLt:])
            result += math.fsum(arr[:winRt])
            log.info("left %s right %s" % (winLt, winRt))  # debug print
            for j in range(field_len - 1 + winLt, field_len - 1):
                weigth += arr[j] * weights[nw]
                nw += 1
            for j in range(0, winRt):
                weigth += arr[j] * weights[nw]
                nw += 1
        elif winRt > field_len:
            result = math.fsum(arr[winLt:])
            result += math.fsum(arr[:winRt - field_len])
            log.info("left %s right %s" % (winLt, winRt))  # debug print
            for j in range(winLt, field_len):
                weigth += arr[j] * weights[nw]
                nw += 1
            for j in range(0, winRt - field_len):
                weigth += arr[j] * weights[nw]
                nw += 1
        else:
            result = math.fsum(arr[winLt:winRt])
            log.info("left %s right %s" % (winLt, winRt))  # debug print
            for j in range(winLt, winRt):
                weigth += arr[j] * weights[nw]
                nw += 1
        return result, round(weigth, 6)

    # count_window_value starts
    window_values = []
    weight_values = []
    weights = count_weights(window_size)
    field_len = len(arr)
    if window_size >= field_len:
        return None
    lt = window_size // 2
    rt = window_size - lt
    # calculate window sum and weight
    for i in range(0, field_len):
        s, w = count_window_value(i)
        window_values.append(s)
        weight_values.append(w)
    # find max/min value and position
    ind, criVal = 0, 0
    for i in range(0, field_len):
        if criterion(weight_values[i], criVal):
            ind = i
            criVal = weight_values[i]
    # logging all arrays
    for i in range(0, field_len - 1):
        log.info("%s - %s \t %s - %s" % (i, arr[i], window_values[i], weight_values[i]))
    log.info("max value = %s in pos %s with weight = %s" % (max(window_values), ind, criVal))
    return ind, window_values[ind]


if __name__ == '__main__':
    logging.basicConfig(filename="z0_win_search_l.log", filemode='w', level=logging.INFO)
    log = logging.getLogger()
    data = [i for i in itertools.repeat(1, 101)]
    pos = len(data) // 2 - 5
    print(f'max position = {pos}')
    data[pos] += 10
    data[pos - 2] += 5
    data[pos + 2] += 5
    print(window_search(window_size=35,
                        arr=data,
                        criterion=lambda a, b: a > b))
