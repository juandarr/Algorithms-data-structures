def substrCount(n, s):
    counter = n
    for i in range(n):
        t = s[i]
        k = 1
        sub = {s[i]: 1}
        for j in range(i + 1, n):
            t += s[j]
            k += 1
            if s[j] in sub:
                sub[s[j]] += 1
            else:
                sub[s[j]] = 1
            if len(sub) == 1:
                counter += 1
            elif len(sub) == 2:
                if k % 2 == 1:
                    tmpChar = t[k // 2]
                    if tmpChar in sub:
                        if sub[tmpChar] == 1:
                            counter += 1
            else:
                break
    return counter


file = open("input15.txt", "r")
data = file.readlines()
idx = 0
for d in data:
    if idx == 0:
        n = int(d)
        idx += 1
    else:
        st = d
# st = "mnonopoo"
print(substrCount(n, st))
