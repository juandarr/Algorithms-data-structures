import math


def minTime(machines, goal):
    production = {}
    for m in machines:
        if m in production:
            production[m] += 1
        else:
            production[m] = 1
    d = 1
    min = 0
    max = float("inf")
    for _ in range(30):
        d *= 10
        s = 0
        for p in production:
            s += (d // p) * production[p]
        if s > goal:
            max = d
            break
    s = 0
    while s != goal:
        d = min + math.ceil((max - min) / 2)
        s = 0
        for p in production:
            s += (d // p) * production[p]
        if s > goal:
            max = d
        elif s < goal:
            min = d
        if max - min == 1:
            d = max
            break
    if s == goal:
        while s == goal:
            d -= 1
            s = 0
            for p in production:
                s += (d // p) * production[p]
        return d + 1
    else:
        return d


def minTime_initial_draft(machines, goal):
    production = {}
    mul = 1
    for m in machines:
        if m in production:
            production[m] += 1
        else:
            production[m] = 1
            mul *= m
    num = 1
    for p in production:
        num *= p
    den = 0
    for p in production:
        val = mul // p
        den += production[p] * val
    return math.ceil(goal * num / den)


if __name__ == "__main__":
    f = open("minTime-test2.txt", "r")
    lines = f.readlines()
    nGoal = lines[0].split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, lines[1].rstrip().split()))

    ans = minTime(machines, goal)
    print(ans)

    f.close()
