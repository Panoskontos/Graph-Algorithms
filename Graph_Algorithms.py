# ----------------------- Directed Graphs------------------------------
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

# -------------------DFS---------------------
# DFS uses STACK
# in PYTHON it will be list methods
# append(), pop()
# DFS iteration


def DFS(graph, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        # to keep track of the order
        print(current)
        # check the neighbors
        # last one will be the next in order
        for i in graph[current]:
            stack.append(i)


# DFS Recursion
def DFS_Recursion(graph, source):
    print(source)
    for i in graph[source]:
        DFS_Recursion(graph, i)


# -------------------BFS-----------------------

# BFS uses Queue
# in PYTHON it will be list methods
# append(), pop(0)
def BFS(graph, source):
    Queue = [source]
    while len(Queue) > 0:
        current = Queue.pop(0)
        # to keep track of the order
        print(current)
        # check the neighbors
        # last one will be the next in order
        for i in graph[current]:
            Queue.append(i)


# Find if graph has path problem
# Solution works like BFS
def hasPath(graph, source, dst):
    if source == dst:
        return True
    # print(source) to see the path
    for i in graph[source]:
        if hasPath(graph, i, dst):
            return True
    return False


# ----------------------- Undirected Grapghs ---------------------------
# If you don't have graph
# helper function if i have only edges
edges = [
    ['a', 'b'],
    ['k', 'a'],
    ['l', 'm'],
    ['m', 'k'],
    ['o', 'n']
]


def buildGraph(edges):
    graph = {}
    for i in edges:
        a, b = i[::]
        if (a not in graph):
            graph[a] = []
        if (b not in graph):
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


# Example graph with cycles , we will not use it
# Un_graph = {
#     'i': ['j', 'k'],
#     'j': ['i'],
#     'k': ['i', 'm', 'l'],
#     'm': ['k'],
#     'l': ['k'],
#     'o': ['n'],
#     'n': ['o'],
# }

# What if your graph has a cycle?
# SOLUTION | we will use visited array

# First let's create our graph
graph = buildGraph(edges)


def has_Path_Undirected(graph, source, dst, visited):
    # check if visited
    if source in visited:
        return False
    visited.append(source)
    # cehck if dst
    if (source == dst):
        return True
    # check the neighbors BFS style
    for i in graph[source]:
        if has_Path_Undirected(graph, i, dst, visited):
            return True
    return False


print(has_Path_Undirected(graph, 'a', 'l', []))