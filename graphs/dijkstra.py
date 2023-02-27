import heapq


def read_graph(filename):
    lines = open(filename, 'r')
    lines = lines.readlines()
    graph = {}
    for line in lines:
        line = line.strip().split('\t')
        graph[line[0]] = {}
        for w in line[1:]:
            tmp = w.split(',')
            graph[line[0]][tmp[0]] = int(tmp[1])
    return graph


def dijkstra(graph, start):
    # Retrieve node list from graph adjacency representation
    V = set()
    for v in graph:
        V.add(v)
        for e in graph[v]:
            V.add(e)
    # Define starting point
    current_node = start
    # Storage of shortest path to each node
    A = {}
    # Shortest path to starting node
    A[current_node] = 0
    X = set()
    # The set of explored vertices
    X.add(current_node)
    # Heap to store shortest path candidates
    h = []
    node_data = (0, current_node)

    while X != V:
        # For each vortex at the end of the edge, store Dijstra greedy criteria
        for w in graph[current_node]:
            heapq.heappush(h, (A[current_node]+graph[current_node][w], w))
        # While each vertex candidate is in explored, find new candidate
        while current_node in X:
            node_data = heapq.heappop(h)
            current_node = node_data[1]
        # Minimum value to candidate is indeed its shortest path
        X.add(current_node)  # Store in set of explored vertices
        A[current_node] = node_data[0]  # Store shortest path
    return A


def test_dijkstra():
    # Test program: finds the shortest distance to each vertex in the graph
    graph = {'s': {'v': 1, 'w': 4}, 'v': {'t': 6, 'w': 2}, 'w': {'t': 3}}
    A = dijkstra(graph, 's')
    h = []
    for v in A:
        h.append((A[v], v))
    heapq.heapify(h)
    assert tuple(h) == ((0, 's'), (1, 'v'), (3, 'w'), (6, 't')), 'The shortest\
            path to every other location in graph doesn\'t  match, TEST FAILED'
    print('The shortes path to every other location in graph matches, \
            TEST PASSED')


if __name__ == "__main__":
    test_dijkstra()
    filename = 'resources/dijkstraData.txt'
    # Graph in adjacency representation
    graph = read_graph(filename)
    A = dijkstra(graph, '1')
    nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    sol = ''
    for node in nodes:
        if str(node) in A:
            sol += str(A[str(node)])+','
        else:
            sol += str(10**6)+','
    print(sol[:-1])
