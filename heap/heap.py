from math import floor


def parent(index: int) -> int:
    return floor((index-1)/2)


def left(index: int) -> int:
    return 2 * index + 1


def right(index: int) -> int:
    return 2 * index + 2


def show_ancestry(ar):
    print("Node  Parent  Left  Right")
    for idx, i in enumerate(ar):
        n, p, l, r = (len(ar), parent(idx), left(idx), right(idx))
        print(i, ar[p] if p < n and p >= 0 else None,
              ar[l] if l < n else None,
              ar[r] if r < n else None)


ar = [10, 7, 2, 5, 1]
show_ancestry(ar)
