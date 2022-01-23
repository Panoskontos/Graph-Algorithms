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
    ['o', 'n'],
    ['t', 'u'],
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


# print(has_Path_Undirected(graph, 'a', 'l', []))


# PROBLEM
# How many seperate components are in a graph?
# This is called connected components problem
# We will go through all nodes, create a visited array and implements DFS, every time it completes we will add 1

def countComponents(graph):
    visited = []
    count = 0
    for i, j in graph.items():
        if i not in visited:
            if explore(graph, i, visited):
                count += 1
    return count

# will can dfs or bfs


def explore(graph, source, visited):
    # start from source and work with dfs
    if source in visited:
        return False
    # append visited
    visited.append(source)
    for i in graph[source]:
        explore(graph, i, visited)
    # if finished it means we completed the components
    return True


# What is the Largest component in an undirected graph?

def largestComponents(graph):
    visited = []
    largest = 0
    for i, j in graph.items():
        if i not in visited:
            size = exploreSize(graph, i, visited)
            if size > largest:
                largest = size
    return largest


def exploreSize(graph, source, visited):
    # if visited return 0
    if source in visited:
        return 0
    # append visited
    size = 1
    visited.append(source)
    for i in graph[source]:
        size += exploreSize(graph, i, visited)
    # if finished it means we completed the components
    return size


print(largestComponents(graph))
