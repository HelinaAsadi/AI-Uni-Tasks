import time
from collections import deque

goal = tuple(range(1, 16)) + (0,)  # goal is (1, 2, 3, ..., 15, 0)


def heuristic(state):  # h(n) = Manhattan Distance
    distance = 0
    for i, val in enumerate(state):  # gets a tuple as input
        if val == 0:  # skips the empty node
            continue
        correct_pos = val - 1  # correct position for each node is 1 index before its value
        x1, y1 = divmod(i, 4)  # converts a flat index into (row, column) coordinates
        x2, y2 = divmod(correct_pos, 4)
        distance += abs(x1 - x2) + abs(y1 - y2)  # sum of the vertical and horizontal distances
    return distance


def getNeighbors(state):  # getting a tuple of the current state of elements
    neighbors = []
    zero = state.index(0)  # finds the place of the 0 node
    x, y = divmod(zero, 4)  # getting its coordinates

    def swipe(new_zero):  # for swipping elements
        swipeList = list(state)  # making a mutable list
        swipeList[zero], swipeList[new_zero] = swipeList[new_zero], swipeList[zero]
        return tuple(swipeList)

    # filtering only doable and permitted swipes
    if x > 0:  # Up (if noy at most top)
        neighbors.append(swipe(zero - 4))
    if x < 3:  # Down (if not at most down)
        neighbors.append(swipe(zero + 4))
    if y > 0:  # Left (if not at most left)
        neighbors.append(swipe(zero - 1))
    if y < 3:  # Right (if not at most right)
        neighbors.append(swipe(zero + 1))

    return neighbors


def astar(initialState):
    startT = time.time()  # to report search execution time

    """
    this priority queue will hold tuples as (f, g, state, path)
    f = evaluation factor ; f(n) = g(n) + h(n)
    g(n) = traversed cost/distance so far
    state = the current puzzle state (a tuple of numbers)
    path = the list of states taken to reach this point

    """

    f0 = heuristic(initialState)
    priorityQueue = deque([(f0, 0, initialState, [])])
    visited = set()

    while priorityQueue:
        '''
        Sorting by the first element which is f
        by sorting, queue performs as a priority queue

        '''
        priorityQueue = deque(sorted(priorityQueue, key=lambda x: x[0]))
        f, g, currentState, path = priorityQueue.popleft()

        if currentState in visited:
            continue

        visited.add(currentState)
        path = path + [currentState]

        if currentState == goal:
            return {
                "path": path,
                "moves": len(path) - 1,
                "time": time.time() - startT
            }

        for neighbor in getNeighbors(currentState):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                priorityQueue.append((new_f, new_g, neighbor, path))

    return {
        "path": [],
        "moves": 0,
        "time": time.time() - startT,
        "message": "Unsolvable"
    }