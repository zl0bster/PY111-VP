from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    def merge(contLt: List[int], contRt: List[int]) -> List[int]:
        result = []
        while contLt or contRt:
            if not contLt:
                result += contRt
                break
            if not contRt:
                result += contLt
                break
            if contLt[0] <= contRt[0]:
                result.append(contLt.pop(0))
                continue
            else:
                result.append(contRt.pop(0))
                continue
        return result

    if len(container) == 1:
        return container
    contMiddle = len(container) // 2
    lt = container[:contMiddle]
    rt = container[contMiddle:]
    return merge(sort(lt), sort(rt))
