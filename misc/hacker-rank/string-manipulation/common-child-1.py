def preprocess(s1, s2):
    toRemove1 = []
    for idx1, i in enumerate(s1):
        present = False
        for j in s2:
            if i == j:
                present = True
                break
        if not present:
            toRemove1.append(idx1)
    toRemove2 = []
    for idx2, j in enumerate(s2):
        present = False
        for i in s1:
            if i == j:
                present = True
                break
        if not present:
            toRemove2.append(idx2)
    tmp1 = list(s1)
    tmp2 = list(s2)
    for idx in reversed(toRemove1):
        tmp1.pop(idx)
    for idx in reversed(toRemove2):
        tmp2.pop(idx)
    d_tmp2 = {}
    for idx, i in enumerate(tmp2):
        if i in d_tmp2:
            d_tmp2[i].append(idx)
        else:
            d_tmp2[i] = [idx]
    return tmp1, d_tmp2


def commonChild(s1, d_s2, idx, inc):
    m = inc
    for idx1, i in enumerate(s1):
        if i in d_s2:
            for j in d_s2[i]:
                if j > idx:
                    tmp = commonChild(s1[idx1 + 1 :], d_s2, j, inc + 1)
                    if tmp > m:
                        m = tmp
    return m


s1, d_s2 = preprocess(
    "ELGGYJWKTDHLXJRBJLRYEJWVSUFZKYHOIKBGTVUTTOCGMLEXWDSXEBKRZTQUVCJNGKKRMUUBACVOEQKBFFYBUQEMYNENKYYGUZSP",
    "FRVIFOVJYQLVZMFBNRUTIYFBMFFFRZVBYINXLDDSVMPWSQGJZYTKMZIPEGMVOUQBKYEWEYVOLSHCMHPAZYTENRNONTJWDANAMFRX",
)
# s1, d_s2 = preprocess(
#     "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS",
#     "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC",
# )
# s1, d_s2 = preprocess("HARRY", "SALLY")
# s1, d_s2 = preprocess("ABCD", "ABDC")
print(s1, d_s2)
print(
    commonChild(
        s1,
        d_s2,
        -1,
        0,
    )
)
