def commonChild(s1, s2, inc):
    tmp = [inc]
    for idx1, i in enumerate(s1):
        for idx2, j in enumerate(s2):
            if i == j:
                tmp.append(commonChild(s1[idx1 + 1 :], s2[idx2 + 1 :], inc + 1))
    return max(tmp)


print(commonChild("abcdef", "fbdamn", 0))
