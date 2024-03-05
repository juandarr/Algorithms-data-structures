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
    for _ in range(15):
        d *= 10
        s = 0
        for p in production:
            s += (d // p) * production[p]
        if s > goal:
            max = d
            break
    print(min, max)
    s = 0
    while s != goal:
        d = min + (max - min) // 2
        print(d, min, max)
        s = 0
        for p in production:
            s += (d // p) * production[p]
        if s > goal:
            max = d
        elif s < goal:
            min = d
    while s == goal:
        d -= 1
        s = 0
        for p in production:
            s += (d // p) * production[p]
    return d + 1


print("Solution: ", minTime([4, 5, 6], 12))
