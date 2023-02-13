from functools import reduce


# Depth first search algorithm using recursion
def topological_dfs(graph, start):
    global f
    global n
    explored.add(start)
    if start in graph:
        for vortex in reversed(graph[start]):
            if vortex not in explored:
                explored.add(vortex)
                topological_dfs(graph, vortex)
    f[start] = n
    n -= 1
    return f


def test_topological_dfs(graph, start, i):
    # Check if the result is what's expected
    result = topological_dfs(graph, start)
    # Verify that for every arc (v, u), f(v) < f(u)
    result = [f[v] < f[e] for v in graph for e in graph[v]]
    assert reduce(lambda x, y: x == y, result, True), f"Expected \
    all f(v) < f(u) for every arc (v, u)"
    print("Test graph {0} passed".format(i))


if __name__ == "__main__":
    # Third graph is connected cyclic
    graphs = [{'A': ['B', 'C'], 'B':['D', 'E'], 'C': ['F']},
              {'A': ['B', 'C'], 'B': ['D'], 'C': ['D']},
              {'A': ['V', 'W'], 'V': ['W', 'T'], 'W':['T'], 'T':['A']}]
    for idx, graph in enumerate(graphs[:-1]):
        explored = set()
        n = len(set(graph.keys()).union(
            reduce(lambda x, y: set(x).union(set(y)),
                [ws for n in graph for ws in graph[n]], set())))
        f = {}
        test_topological_dfs(graph, 'A', idx+1)
