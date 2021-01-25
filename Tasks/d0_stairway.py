from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    def lazy_way(stairway):
        def get_cost(n):
            if n == 0 or n == 1:
                return stairway[n]
            return stairway[n] + min(get_cost(n - 1), get_cost(n - 2))

        return get_cost(len(stairway) - 1)

    def direct_way(stairway):
        last = len(stairway)
        nodeCost = [0] * last
        nodeCost[0] = stairway[0]
        nodeCost[1] = stairway[1]  # +stairway[1]
        for i in range(2, last):
            nodeCost[i] = stairway[i] + min(nodeCost[i - 1], nodeCost[i - 2])
            print(i, stairway[i], nodeCost[i], min(stairway[i - 1], stairway[i - 2]))
        print('*' * 20)
        return nodeCost[-1]

    return direct_way(stairway)

    # pos = 0
    # last = len(stairway)
    # minCost = stairway[0]
    # pos = 0
    # last = len(stairway)
    # while pos < last - 1:
    #     nextOne = stairway[pos + 1]
    #     if pos == last - 2:
    #         pos += 1
    #         minCost += nextOne
    #         continue
    #     afterNext = stairway[pos + 2]
    #     if nextOne >= afterNext:
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

    # pos = len(stairway) - 1
    # minCost = stairway[pos]
    # while pos > 1:
    #     nextOne = stairway[pos - 1]
    #     afterNext = stairway[pos - 2]
    #     if (nextOne >= afterNext) or (pos == 2):
    #         pos -= 2
    #         minCost += afterNext
    #     else:
    #         pos -= 1
    #         minCost += nextOne
    #     print(pos, stairway[pos], minCost)
    # if pos == 1:
    #     minCost += stairway[0]
    # print(minCost)
    # print('*' * 20)
    # return minCost


if __name__ == '__main__':
    test_st = [4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2]
    print(stairway_path(test_st))
