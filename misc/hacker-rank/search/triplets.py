def triplets(a, b, c):
    tr = {}
    for j in b:
        for i in a:
            if j >= i:
                for k in c:
                    if j >= k:
                        if (i, j, k) not in tr:
                            tr[(i, j, k)] = 1
            else:
                continue
    return len(tr)


print(triplets([1, 3, 5], [2, 3], [1, 2, 3]))
