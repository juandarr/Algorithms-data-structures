import copy


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
    return tmp1, tmp2


def commonChild(s1, s2, inc):
    m = inc
    for idx1, i in enumerate(s1):
        for idx2, j in enumerate(s2):
            if i == j:
                tmp = commonChild(s1[idx1 + 1 :], s2[idx2 + 1 :], inc + 1)
                if tmp > m:
                    m = tmp
    return m


s1, s2 = preprocess(
    "ELGGYJWKTDHLXJRBJLRYEJWVSUFZKYHOIKBGTVUTTOCGMLEXWDSXEBKRZTQUVCJNGKKRMUUBACVOEQKBFFYBUQEMYNENKYYGUZSP",
    "FRVIFOVJYQLVZMFBNRUTIYFBMFFFRZVBYINXLDDSVMPWSQGJZYTKMZIPEGMVOUQBKYEWEYVOLSHCMHPAZYTENRNONTJWDANAMFRX",
)
# s1, s2 = preprocess(
#     "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS",
#     "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC",
# )
# s1, s2 = preprocess("HARRY", "SALLY")
print(s1, s2)
print(
    commonChild(
        s1,
        s2,
        0,
    )
)
