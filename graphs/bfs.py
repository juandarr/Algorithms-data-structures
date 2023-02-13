# Breath first search algorithm
def bfs(graph, start):
    # Queue used to explore layers of graph, one by one
    to_explore = [start]
    # Set of explored vertices
    explored = set(start)
    # Path to store visited nodes, in order
    path = [start]
    while to_explore:
        currentVortex = to_explore.pop(0)
        if currentVortex not in explored:
            explored.add(currentVortex)
            path.append(currentVortex)
        for vortex in graph[currentVortex]:
            if vortex not in explored:
                to_explore.append(vortex)
    return path


def test_bfs(graph, start):
    # Check if the result is what's expected
    result = bfs(graph, start)
    assert result == ['A', 'B', 'C', 'D', 'E', 'F'], f"Expected {result=} to\
            be {['A', 'B', 'C', 'D', 'E', 'F']}"
    print("Test passed")


if __name__ == "__main__":
    graph = {}
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D', 'E']
    graph['C'] = ['A', 'F']
    graph['D'] = ['B']
    graph['E'] = ['B', 'F']
    graph['F'] = ['C', 'E']
    test_bfs(graph, 'A')
