import resource
import sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**6)


def read_graph(connections):
    """A function to read the graph"""
    g = {}
    g_rev = {}
    n = 0
    for connection in connections:
        connection = connection.strip().split(' ')
        nmax = max(int(connection[0]), int(connection[1]))
        if n < nmax:
            n = nmax
        if connection[0] not in g:
            g[connection[0]] = [connection[1]]
        else:
            g[connection[0]].append(connection[1])
        if connection[1] not in g_rev:
            g_rev[connection[1]] = [connection[0]]
        else:
            g_rev[connection[1]].append(connection[0])
    return g, g_rev, n


# Depth first search algorithm using recursion
def dfs(graph, start):
    global t
    global f
    global leader
    global explored
    if start in explored:
        return
    explored.add(start)
    if s in leader:
        leader[s] += 1
    else:
        leader[s] = 1
    if start in graph:
        for vortex in graph[start]:
            if vortex not in explored:
                dfs(graph, vortex)
    if start not in f:
        t += 1
        f[start] = t


def dfs_loop(graph, n):
    global explored
    explored = set()

    global t
    t = 0
    global f
    f = {}

    global s
    s = None
    global leader
    leader = {}

    for i in range(n, 0, -1):
        i_str = str(i)
        if i_str not in explored:
            s = i_str
            dfs(graph, i_str)
    return sorted(leader.values(), reverse=True)[0:5]


def dfs_scc(connections):
    graph, graph_rev, n = read_graph(connections)

    dfs_loop(graph_rev, n)

    new_graph = {}
    for vortex in graph:
        new_graph[str(f[vortex])] = []
        for end in graph[vortex]:
            new_graph[str(f[vortex])].append(str(f[end]))

    components = dfs_loop(new_graph, n)
    components = components + [0]*max(5-len(components), 0)
    return ','.join([str(i) for i in components])


def test_dfs_scc():
    connections = \
        """7 1
        4 7
        1 4
        9 7
        6 9
        3 6
        9 3
        8 6
        8 5
        2 8
        5 2"""
    connections = connections.split('\n')
    result = dfs_scc(connections)
    assert result == '3,3,3,0,0',\
        'The number of strongly connected components doesn\'t  match, TEST FAILED'
    print('The number of strongly connected components matches, TEST PASSED')


# Answer: 434821,968,459,313,211
if __name__ == "__main__":
    test_dfs_scc()
    filename = '../resources/web-graph.txt'
    connections = open(filename, 'r')
    connections = connections.readlines()
    components = dfs_scc(connections)
    print("The number of strongly connected components is {0}"
          .format(components))
