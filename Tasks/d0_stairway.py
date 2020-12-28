from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    # minCost = stairway[0]
    # pos = 0
    # last = len(stairway)
    # while pos < last - 1:
    #     nextOne = stairway[pos + 1]
    #     afterNext = stairway[pos + 2]
    #     if (nextOne >= afterNext) or (pos == last - 2):
    #         pos += 2
    #         minCost += afterNext
    #     else:
    #         pos += 1
    #         minCost += nextOne
    #     print(pos, stairway[pos], minCost)
    # if pos < (last - 1):
    #     minCost += stairway[last - 1]
    # print(minCost)
    # print('*' * 20)
    # return minCost

    pos = len(stairway) - 1
    minCost = stairway[pos]
    while pos > 1:
        nextOne = stairway[pos - 1]
        afterNext = stairway[pos - 2]
        if (nextOne >= afterNext) or (pos == 2):
            pos -= 2
            minCost += afterNext
        else:
            pos -= 1
            minCost += nextOne
        print(pos, stairway[pos], minCost)
    if pos == 1:
        minCost += stairway[0]
    print(minCost)
    print('*' * 20)
    return minCost


if __name__ == '__main__':
    test_st = [4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2]
    print(stairway_path(test_st))
