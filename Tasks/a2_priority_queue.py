"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

pri_queue = {0: [],
             1: [],
             2: [],
             3: [],
             4: [],
             5: [],
             6: [],
             7: [],
             8: [],
             9: [],
             10: []
             }


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    pri_queue[priority].append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    for i in range(0, 11):
        if pri_queue[i]:
            result = pri_queue[i].pop(0)
            return result
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    queue = pri_queue[priority]
    if queue:
        if ind < len(queue):
            return queue[ind]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    for i in range(0, 11):
        if pri_queue[i]:
            pri_queue[i].clear()
    return None
