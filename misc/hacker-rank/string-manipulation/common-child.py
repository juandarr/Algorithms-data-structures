def commonChild(s1, s2):
    for idx1, i in enumerate(s1):
        for idx2, j in enumerate(s2):
            if i == j:
                return 1 + commonChild(s1[idx1 + 1 :], s2[idx2 + 1 :])
            continue
    return 0
