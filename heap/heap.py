from math import floor
from typing import Optional


class Heap(object):
    # def __init__(self, ar):
    #     self.ar = []
    #     for i in ar:
    #         self.insert(i)
    def __init__(self, ar):
        self.ar = ar
        n = len(ar)
        for i in range(floor(len(ar)/2)-1, -1, -1):
            idx = i
            old_idx = n-1
            print(self.ar, '-')
            while idx != old_idx and idx < floor(n/2):
                old_idx = idx
                idx = self.bubble_down(idx)
                print(self.ar)

    @staticmethod
    def parent(index: int) -> int:
        return floor((index-1)/2)

    @staticmethod
    def left(index: int) -> int:
        return 2 * index + 1

    @staticmethod
    def right(index: int) -> int:
        return 2 * index + 2

    def is_empty(self):
        return len(self.ar) == 0

    def peek(self):
        return self.ar[0]

    def show_table(self) -> None:
        print("Node  Parent  Left  Right")
        for idx, i in enumerate(self.ar):
            n, p, l, r = (len(self.ar), self.parent(idx), self.left(idx),
                          self.right(idx))
            i_str = str(i)
            i_str = i_str+' '*(6-len(i_str))
            p_str = str(self.ar[p] if p < n and p >= 0 else None)
            p_str = p_str+' '*(8-len(p_str))
            l_str = str(self.ar[l] if l < n else None)
            l_str = l_str+' '*(6-len(l_str))
            r_str = str(self.ar[r] if r < n else None)
            r_str = r_str+' '*(5-len(r_str))
            print(i_str+p_str+l_str+r_str)

    def bubble_up(self, idx: int) -> int:
        idx_p = self.parent(idx)
        if self.ar[idx_p] > self.ar[idx]:
            tmp = self.ar[idx_p]
            self.ar[idx_p] = self.ar[idx]
            self.ar[idx] = tmp
            return idx_p
        else:
            return idx

    def bubble_down(self, idx: int) -> int:
        idx_l = self.left(idx)
        idx_r = self.right(idx)
        tmp_idx = idx
        n = len(self.ar)
        if idx_l < n and self.ar[idx_l] < self.ar[tmp_idx]:
            tmp_idx = idx_l
        if idx_r < n and self.ar[idx_r] < self.ar[tmp_idx]:
            tmp_idx = idx_r
        if tmp_idx != idx:
            tmp = self.ar[idx]
            self.ar[idx] = self.ar[tmp_idx]
            self.ar[tmp_idx] = tmp
            return tmp_idx
        return idx

    def insert(self, value: int) -> None:
        self.ar.append(value)
        idx = len(self.ar)-1
        old_idx = 0
        while (old_idx != idx and idx > 0):
            old_idx = idx
            idx = self.bubble_up(idx)

    def remove(self, index: int = 0) -> Optional[int]:
        if len(self.ar) == 0:
            return None

        last = self.ar.pop()
        if len(self.ar) == 0:
            return last
        value_at_index = self.ar[index]
        self.ar[index] = last
        idx = index
        n = len(self.ar)
        old_idx = n-1
        while (idx != old_idx and idx < floor(n / 2)):
            old_idx = idx
            p_idx = self.parent(idx)
            if p_idx >= 0 and self.ar[p_idx] > self.ar[idx]:
                idx = self.bubble_up(idx)
            else:
                idx = self.bubble_down(idx)
        return value_at_index

    def index(self, value: int) -> int:
        return self.ar.index(value)

    # Next steps:
    # TODO Add comments and improve code


ar = [10, 7, 3, 5, 1, 2, 8, 4]
h = Heap(ar)
h.show_table()
