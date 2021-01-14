"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple

# import networkx as nx

binTree = {}
rootNode = None


class Node:
    def __init__(self, key: int, value: Any) -> None:
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    def is_full(self):
        if self.left and self.right:
            return True
        return False

    def __str__(self):
        result = f"({self.key}) ^{self.parent} <{self.left} >{self.right}"
        return result


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global rootNode, binTree
    if key in binTree.keys():
        binTree[key].value = value
        return None
    node = Node(key=key, value=value)
    binTree[key] = node
    if rootNode is None:
        rootNode = key
        return None
    curNode = rootNode
    while True:
        if key < curNode:
            if binTree[curNode].left is None:
                binTree[curNode].left = key
                binTree[key].parent = curNode
                break
            else:
                curNode = binTree[curNode].left
                continue
        else:
            if binTree[curNode].right is None:
                binTree[curNode].right = key
                binTree[key].parent = curNode
                break
            else:
                curNode = binTree[curNode].right
                continue
    return None


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    global rootNode, binTree
    curNode = rootNode
    while True:
        if curNode == key:
            result = binTree[curNode].value
            # todo переподключить поля parent, left and right af affected nodes
            return result
        if key < curNode:
            if binTree[curNode].left:
                curNode = binTree[curNode].left
                continue
            else:
                break
        else:
            if binTree[curNode].right:
                curNode = binTree[curNode].right
                continue
            else:
                break
    return None


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    global rootNode, binTree
    curNode = rootNode
    while True:
        if curNode == key:
            return binTree[curNode].value
        if key < curNode:
            if binTree[curNode].left:
                curNode = binTree[curNode].left
                continue
            else:
                break
        else:
            if binTree[curNode].right:
                curNode = binTree[curNode].right
                continue
            else:
                break
    raise KeyError


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    global rootNode, binTree
    binTree.clear()
    rootNode = None
    return None


def showTree():
    print('+' * 12)
    for node in binTree:
        print(node)
