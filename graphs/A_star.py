from heapq import heappush, heappop


def a_star(start, goal, graph):
    open_set = [(0, start)]  # (f_score, node)
    came_from = {}  # node -> node
    g_score = {start: 0}  # node -> g_score
    f_score = {start: g_score[start] +
               heuristic_cost_estimate(start, goal)}  # node -> f_score

    while open_set:
        current = heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + cost(current, neighbor)
            if neighbor not in g_score or\
                    tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + \
                    heuristic_cost_estimate(neighbor, goal)
                heappush(open_set, (f_score[neighbor], neighbor))
    return None


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def heuristic_cost_estimate(start, goal):
    # Euclidean distance
    return ((start[0] - goal[0]) ** 2 + (start[1] - goal[1]) ** 2) ** 0.5


def cost(current, neighbor):
    # Example cost function
    return 1


graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 2), (0, 0)],
    (0, 2): [(0, 1)],
    (1, 0): [(0, 0), (2, 0)],
    (2, 0): [(1, 0)],
}

start = (0, 0)
goal = (0, 2)

print(a_star(start, goal, graph))  # [(0, 0), (0, 1), (0, 2)]
