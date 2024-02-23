def substrCount(n, s):
    counter = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i : j + 1]
            print(sub)
            tmp = set(sub)
            if len(tmp) == 1:
                counter += 1
            elif len(tmp) == 2:
                k = len(sub)
                if k % 2 == 1:
                    tmpChar = sub[k // 2]
                    c = 0
                    special = True
                    for t in sub:
                        if t == tmpChar:
                            c += 1
                            if c > 1:
                                special = False
                                break
                    if special:
                        counter += 1
    return counter


st = "mnonopoo"
substrCount(len(st), st)
