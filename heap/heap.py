from math import floor


def parent(index: int) -> int:
    return floor((index-1)/2)


def left(index: int) -> int:
    return 2 * index + 1


def right(index: int) -> int:
    return 2 * index + 2
