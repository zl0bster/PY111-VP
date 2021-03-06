"""
My little Queue
"""
from typing import Any

my_queue = []  # start at the left, end at the right


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    my_queue.insert(0, elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if my_queue:
        result = my_queue.pop()
    else:
        result = None
    return result


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if ind < (len(my_queue)):
        result = my_queue[-1 - ind]
    else:
        result = None
    return result


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    my_queue.clear()
    return None


if __name__ == '__main__':
    enqueue(1)
    enqueue(13)
    enqueue(2)
    print(my_queue)
    print(peek(12))
    print(dequeue())
