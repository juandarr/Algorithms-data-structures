def triplets(a, b, c):
    a = set(a)
    b = set(b)
    c = set(c)
    a_s = sorted(a)
    c_s = sorted(c)
    count = 0
    for j in b:
        for i in a_s:
            if j >= i:
                for k in c_s:
                    if j >= k:
                        count += 1
                    else:
                        break
            else:
                break
    return count


print(triplets([1, 3, 5], [2, 3], [1, 2, 3]))
