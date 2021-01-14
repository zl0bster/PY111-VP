from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    def sort(container: List[int]) -> List[int]:
        """
        Sort input container with quick sort
        1. Неким образом определяем опорный элемент
        2. Идем по массиву двумя счетчиками – слева направо и справа налево
        3. Увеличиваем левый счетчик, пока он не встретит элемент больше или равный опорному
        4. Уменьшаем правый счетчик, пока он не встретит элемент меньше или равный опорному
        5. Меняем элементы местами
        6. Продолжаем уменьшать счетчики и менять элементы аналогичным образом, пока счетчики не встретятся – получаем индекс элемента, левее которого все элементы меньше или равны опорному, а правее – больше опорного
        7. Запускаем рекурсивно алгоритм от части левее опорного элемента и правее опорного элемента
        :param container: container of elements to be sorted
        :return: container sorted in ascending order
        """

        def _sort(left, right):
            pivot = left  # 1. Неким образом определяем опорный элемент
            i, j = left + 1, right  # 2. Идем по массиву двумя счетчиками – слева направо и справа налево
            # 3. Увеличиваем левый счетчик, пока он не встретит элемент больше или равный опорному
            while container[left] < container[pivot]:
                i += 1

        _sort(0, len(container) - 1)
        return container

    return container
