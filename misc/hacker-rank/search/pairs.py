def pairs(k, arr):
    d = {}
    for i in arr:
        d[i] = 1
    p = 0
    for i in arr:
        if (i - k) in d:
            p += 1
    return p


print(pairs(2, [1, 5, 3, 4, 2]))
