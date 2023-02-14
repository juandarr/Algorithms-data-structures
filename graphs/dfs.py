# Depth first search algorithm using stacks
def dfs_stack(graph, start):
    # Stack used to explore every vortex in graph, by depth
    to_explore = [start]
    # Set of explored vertices
    explored = set(start)
    # Path to store visited nodes, in order
    path = [start]
    while to_explore:
        currentVortex = to_explore.pop()
        if currentVortex not in explored:
            explored.add(currentVortex)
            path.append(currentVortex)
        for vortex in reversed(graph[currentVortex]):
            if vortex not in explored:
                to_explore.append(vortex)
    return path


# Depth first search algorithm using recursion
def dfs(graph, start):
    global path
    global explored
    if start in explored:
        return
    explored.add(start)
    path.append(start)
    for vortex in graph[start]:
        if vortex not in explored:
            dfs(graph, vortex)
    return path


def test_dfs(graph, start):
    # Check if the result is what's expected
    result = dfs(graph, start)
    assert result == ['A', 'B', 'D', 'E', 'F', 'C'], f"Expected {result=} to\
            be {['A', 'B', 'D', 'E', 'F', 'C']}"
    print("Test passed")


if __name__ == "__main__":
    graph = {}
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D', 'E']
    graph['C'] = ['A', 'F']
    graph['D'] = ['B']
    graph['E'] = ['B', 'F']
    graph['F'] = ['C', 'E']
    explored = set()
    path = []
    test_dfs(graph, 'A')
