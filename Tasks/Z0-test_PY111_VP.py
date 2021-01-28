"""функции имеют имена соответствующие номеру задания"""
from typing import Sequence
import networkx as nx
from random import randint


def task_1(arr: Sequence):
    """Оценить асимптотическую сложность приведенного ниже алгоритма: """
    a = len(arr) - 1  # O(1)
    out = list()  # O(1)
    while a > 0:  # O(n) для всего цикла (!) согласен, здесь , похоже, O(log n) подходит больше
        out.append(arr[a])
        a = a // 1.7
    out.merge_sort()  # O(n log n)


# в итоге САМЫМ долгим будет время сортировки O(n log n), что и определяет время алгоритма


def task_2(n: int, k: int) -> int:
    """Считалочка
    Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
    Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
    (если на каждом новом круге начинать со следующего за вышедшим)
    Игра происходит до тех пор, пока не останется последний человек.
    Для данных N и К дать номер последнего оставшегося человека.
     """
    players = [i for i in range(1, n + 1)]
    nextOut = 0
    while len(players) > 1:  # считать, пока не остался последний
        step = len(players) % k if len(players) >= k else k % len(players)  # остаток от деления большего на меньшее
        nextOut = (nextOut + step) % len(players)  # добавить к номеру текущего
        players.pop(nextOut)
    return players[0]


def task_4(size: int, start: str, finish: str) -> Sequence:
    """
    Навигатор на сетке.
    Дана плоская квадратная двумерная сетка (массив),
    на которой определена стоимость захода в каждую ячейку (все стоимости положительные).
    Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.
    """
    gfx = task_4_net_create(size)

    print(f'стоимость маршрута  = {nx.dijkstra_path_length(gfx, start, finish)}')
    return nx.dijkstra_path(gfx, start, finish)


def task_5(arg: list) -> str:
    """Задача консенсуса DNA ридов
    При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
    Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
    в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
    Т.е. для строк
    ATTA
    ACTA
    AGCA
    ACAA
    консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
    Для входного списка из N строк одинаковой длины построить консенсус-строку.
     """

    def find_most_often_char(pos: int, arg: list) -> str:  # pos starts from 0
        alphabet = {'A': 0,
                    'C': 0,
                    'G': 0,
                    'T': 0
                    }
        for word in arg:
            symbol = word[pos]
            alphabet[symbol] += 1
        symbol_qty = max(alphabet.values())
        for key, value in alphabet.items():
            if symbol_qty == value:
                return key

    result = ""
    for i in range(0, 4):
        result += find_most_often_char(i, arg)
    return result


def task_7():
    """Сорт
    Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
    Задача: отсортировать массив наиболее эффективным способом """

    """Решение:
    создать словарь с ключами от 13 до 25
    за один проход по массиву заполнить словарь количеством соответствующего элемента в массиве
    создать пустой итоговый массив
    заполнить его последовательно каждым ключом словаря в рассчитанном количестве"""

    """{13:1256,
        14:4567,
        ...
        25:7891}
        
        [13,13,...,13,14,14,...25,25]
    """


def task_4_net_create(size: int) -> nx.Graph:
    """ создание квадратной сетки с весами и потом графа с ребрами по сетке """

    def node_name(x: int, y: int) -> str:
        return f'{x}_{y}'

    network = [[randint(1, 10) for _ in range(size)] for _ in range(size)]
    edgeList = []
    relations = [-1, 1]
    for x in range(size):
        for y in range(size):
            cellName = node_name(x, y)
            for relation in relations:
                xCur = x + relation
                if 0 <= xCur < size:
                    cellNearName = node_name(xCur, y)
                    edgeData = (cellName, cellNearName, network[y][xCur])
                    edgeList.append(edgeData)
            for relation in relations:
                yCur = y + relation
                if 0 <= yCur < size:
                    cellNearName = node_name(x, yCur)
                    edgeData = (cellName, cellNearName, network[yCur][x])
                    edgeList.append(edgeData)
    for i, arg in enumerate(edgeList):
        print(i, arg)
    for i, arg in enumerate(network):
        print(i, arg)
    sqr_graph = nx.Graph()
    sqr_graph.add_weighted_edges_from(edgeList)
    return sqr_graph


if __name__ == '__main__':
    print(task_2(5, 12))
    task_5_arg = ['ATTA',
                  'ACTA',
                  'AGCA',
                  'ACAA'
                  ]
    print(task_5(task_5_arg))
    route = task_4(size=8, start='7_0', finish='0_7')
    print(f'маршрут {route}')
