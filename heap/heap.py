from math import floor


def parent(index: int) -> int:
    return floor((index-1)/2)


def left(index: int) -> int:
    return 2 * index + 1


def right(index: int) -> int:
    return 2 * index + 2


def show_ancestry(ar: list[int]) -> None:
    print("Node  Parent  Left  Right")
    for idx, i in enumerate(ar):
        n, p, l, r = (len(ar), parent(idx), left(idx), right(idx))
        i_str = str(i)
        i_str = i_str+' '*(6-len(i_str))
        p_str = str(ar[p] if p < n and p >= 0 else None)
        p_str = p_str+' '*(8-len(p_str))
        l_str = str(ar[l] if l < n else None)
        l_str = l_str+' '*(6-len(l_str))
        r_str = str(ar[r] if r < n else None)
        r_str = r_str+' '*(5-len(r_str))
        print(i_str+p_str+l_str+r_str)


ar = [10, 7, 2, 5, 1]
show_ancestry(ar)

# Continue with more math! and heap operations
