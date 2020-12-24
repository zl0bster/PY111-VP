from typing import Sequence, Optional, Callable
import itertools


def cri_max(a, b):
    return a > b


def window_search(window_size: int, arr: Sequence, criteria: Callable) -> Optional[int]:
    """
    Returns the position of window center in array where criteria is satisfied

    :param window_size: the dimension of window to analize
    :param arr: array where element is to be found
    :return: Index of element where criteria is satisfied
    """

    def count_window_value(index: int) -> float:
        winLt = index - lt
        winRt = index + rt
        # result = None
        if winLt < 0:
            result = sum(arr[winLt:])
            result += sum(arr[:winRt])
        else:
            result = sum(arr[winLt:winRt])
        print(result)
        return result

    win_val = []
    field_len = len(arr)
    if window_size >= field_len:
        return None
    lt = window_size // 2
    rt = window_size - lt
    for i in range(0, field_len):
        win_val.append(count_window_value(0))
    print(win_val)


if __name__ == '__main__':
    data = [i for i in itertools.repeat(1, 100)]
    pos = len(data) // 2 - 5
    print(f'position = {pos}')
    data[pos] += 10
    data[pos - 2] += 5
    data[pos + 2] += 5
    print(data)
    print(window_search(window_size=30, arr=data, criteria=cri_max))
