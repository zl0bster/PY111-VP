"""
My little Stack
"""
from typing import Any

my_stack = [] # вершина - справа

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    my_stack.append(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if my_stack:
        result = my_stack.pop()
    else:
        result = None
    return result


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    if ind < len(my_stack):
        result = my_stack[-1 - ind]
        # result = my_stack[0-ind]
    else:
        result = None
    return result


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    my_stack.clear()
    return None

if __name__ =='__main__':
    push((1, 5, 4))
    push(2)
    push(2)
    push(3)
    push(2)
    print(my_stack)
    print(pop())
    print(my_stack)
    print(peek(15))
    print(my_stack)
    clear()
    print(my_stack)
