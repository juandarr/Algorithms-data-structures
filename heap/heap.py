from math import floor


class Heap(object):
    def __init__(self, ar):
        self.ar = []
        for i in ar:
            self.insert(i)

    @staticmethod
    def parent(index: int) -> int:
        return floor((index-1)/2)

    @staticmethod
    def left(index: int) -> int:
        return 2 * index + 1

    @staticmethod
    def right(index: int) -> int:
        return 2 * index + 2

    def show_ancestry(self) -> None:
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

    def insert(self, value: int) -> None:
        self.ar.append(value)
        idx = len(self.ar)-1
        old_idx = 0
        while (old_idx != idx and idx > 0):
            old_idx = idx
            idx = self.bubble_up(idx)
            print('change', self.ar, idx)


ar = [10, 7, 3, 5, 1, 2, 8, 4]
h = Heap(ar)
h.show_ancestry()
