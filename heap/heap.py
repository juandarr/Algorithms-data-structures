from math import floor
from typing import Optional


class Heap(object):
    def __init__(self, order_criteria: str, nodes: list[int]):
        self.nodes = nodes
        if order_criteria == '>':
            self._comp = self._greater_than
            self.type = 'Max-heap'
        elif order_criteria == '<':
            self._comp = self._less_than
            self.type = 'Min-heap'
        for i in range(floor(len(nodes)/2)-1, -1, -1):
            self.bubble_down(i)

    @staticmethod
    def _less_than(left: int, right: int) -> bool:
        return left < right

    @staticmethod
    def _greater_than(left: int, right: int) -> bool:
        return left > right

    @staticmethod
    def _parent(index: int) -> int:
        return floor((index-1)/2)

    @staticmethod
    def _left(index: int) -> int:
        return 2 * index + 1

    @staticmethod
    def _right(index: int) -> int:
        return 2 * index + 2

    def is_empty(self):
        return len(self.nodes) == 0

    def peek(self):
        return self.nodes[0]

    def index(self, value: int) -> int:
        return self.nodes.index(value)

    def show_table(self) -> None:
        print("Node  Parent  Left  Right")
        for idx, i in enumerate(self.nodes):
            p, l, r = (self._parent(idx), self._left(idx), self._right(idx))
            n = len(self.nodes)
            i_str = str(i)
            i_str = i_str+' '*(6-len(i_str))
            p_str = str(self.nodes[p] if p < n and p >= 0 else None)
            p_str = p_str+' '*(8-len(p_str))
            l_str = str(self.nodes[l] if l < n else None)
            l_str = l_str+' '*(6-len(l_str))
            r_str = str(self.nodes[r] if r < n else None)
            r_str = r_str+' '*(5-len(r_str))
            print(i_str+p_str+l_str+r_str)

    def bubble_up(self, idx: int) -> None:
        old_idx = 0
        while (old_idx != idx and idx > 0):
            old_idx = idx
            idx_p = self._parent(idx)
            if self._comp(self.nodes[idx], self.nodes[idx_p]):
                tmp = self.nodes[idx_p]
                self.nodes[idx_p] = self.nodes[idx]
                self.nodes[idx] = tmp
                idx = idx_p

    def bubble_down(self, idx: int) -> None:
        n = len(self.nodes)
        old_idx = n-1
        while (idx != old_idx and idx < floor(len(self.nodes) / 2)):
            old_idx = idx
            idx_l = self._left(idx)
            idx_r = self._right(idx)
            tmp_idx = idx
            if idx_l < n and self._comp(self.nodes[idx_l],
                                        self.nodes[tmp_idx]):
                tmp_idx = idx_l
            if idx_r < n and self._comp(self.nodes[idx_r],
                                        self.nodes[tmp_idx]):
                tmp_idx = idx_r
            if tmp_idx != idx:
                tmp = self.nodes[idx]
                self.nodes[idx] = self.nodes[tmp_idx]
                self.nodes[tmp_idx] = tmp
                idx = tmp_idx

    def insert(self, value: int) -> None:
        self.nodes.append(value)
        idx = len(self.nodes)-1
        self.bubble_up(idx)

    def remove(self, index: int = 0) -> Optional[int]:
        if len(self.nodes) == 0:
            return None

        last = self.nodes.pop()
        if len(self.nodes) == 0 or index == len(self.nodes):
            return last
        value_at_index = self.nodes[index]
        self.nodes[index] = last

        if index < floor(len(self.nodes) / 2):
            p_idx = self._parent(index)
            if p_idx >= 0 and self._comp(self.nodes[index], self.nodes[p_idx]):
                self.bubble_up(index)
            else:
                self.bubble_down(index)
        return value_at_index

    def replace(self, index: int, value: int):
        self.remove(index)
        self.insert(value)

    # Next steps:
    # TODO Add comments


# ar = [10, 7, 3, 5, 1, 2, 8, 4]
