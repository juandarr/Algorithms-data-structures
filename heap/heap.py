from math import floor
from typing import Optional


class Heap(object):
    """
    Heap class

    Creates a heap from an array of nodes
    """
    def __init__(self, order_criteria: str,
                 nodes: list[int | tuple[int, ...]]):
        """
        Constructor method

        Parameters
        __________
        order_criteria : str
            An string value among '<' for Min-heap and '>' for Max-heap
        nodes : list[int] or list[tuple]
            A list of numbers or tuples. In case of tuples first
            value of each tuple must a number
        """
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
        """
        Compares left and right integers using the less than operation

        Parameters
        ----------
        left: int
            Integer to compare in the left side of the < operator
        right: int
            Integer to compare in the right side of the < operator

        Returns
        -------
        boolean
            A boolean indicating whether left is less than right
        """
        return left < right

    @staticmethod
    def _greater_than(left: int, right: int) -> bool:
        """
        Compares left and right integers using the greater than operation

        Parameters
        ----------
        left: int
            Integer to compare in the left side of the > operator
        right: int
            Integer to compare in the right side of the > operator

        Returns
        -------
        boolean
            A boolean indicating whether left is greather than right
        """
        return left > right

    @staticmethod
    def _parent(index: int) -> int:
        """
        Finds the parent node index of a given child node index

        Parameters
        ----------
        index: int
            Index of child node

        Returns
        -------
        int
            Index of parent node index
        """
        return floor((index-1)/2)

    @staticmethod
    def _left(index: int) -> int:
        """
        Finds the left child node index of a given parent node index

        Parameters
        ----------
        index: int
            Index of parent node

        Returns
        -------
        int
            Index of left child node index
        """
        return 2 * index + 1

    @staticmethod
    def _right(index: int) -> int:
        """
        Finds the right child node index of a given parent node index

        Parameters
        ----------
        index: int
            Index of parent node

        Returns
        -------
        int
            Index of right child node index
        """
        return 2 * index + 2

    def _check_item(self, item: int | tuple[int, ...]) -> Optional[int]:
        """
        Checks that `item` is of instance integer or tuple[int, ...]

        Parameters
        ----------
        item : int, tuple[int, ...]
            Element of heap

        Returns
        -------
        int, None
            Key value of node or None if value can't be retrieved
        """
        if isinstance(item, int):
            return item
        elif isinstance(item, tuple):
            if isinstance(item[0], int):
                return item[0]
            else:
                print("First element of tuple must be an integer")
                return None
        else:
            print("Node element must be an integer or tuple (starting \
                    with an number)")
            return None

    def is_empty(self) -> bool:
        """
        Indicates whether the heap is empty or not

        Returns
        -------
        bool
            True when heap is empty, False otherwise
        """
        return len(self.nodes) == 0

    def peek(self) -> Optional[int | tuple[int, ...]]:
        """
        Peek the heap to find value at the root

        Returns
        -------
        int, tuple[int, ...]
            Return number or tuple, as first value at root of heap
        """
        if len(self.nodes) == 0:
            return None
        else:
            return self.nodes[0]

    def get_key(self, index: int) -> Optional[int]:
        """
        Gets key at `index` node

        Parameters
        ----------
        index : int
            index of the node to retrieve the key from

        Returns
        -------
        int, None
            Returns key of node at `index`. When the node is not an integer
            or a tuple with a number as first element, return None
        """
        return self._check_item(self.nodes[index])

    def index(self, value: int) -> Optional[int]:
        """
        Gets index of node with key `value`

        Parameters
        ----------
        value: int
            Key of node element to find in heap

        Returns
        -------
        int, None
            Index of node element with key `value`, or None if no value
            is found
        """
        for idx, i in enumerate(self.nodes):
            key = self._check_item(i)
            if key == value:
                return idx
        return None

    def show_table(self) -> None:
        """
        Shows a table of element in the heap following the structure
        Node, Parent, Left child and Right child as colmuns
        """
        print("Node  Parent  Left  Right")
        for idx, i in enumerate(self.nodes):
            p, l, r = (self._parent(idx), self._left(idx), self._right(idx))
            n = len(self.nodes)
            i_str = str(self._check_item(i))
            i_str = i_str+' '*(6-len(i_str))
            p_str = str(self.get_key(p) if p < n and p >= 0 else None)
            p_str = p_str+' '*(8-len(p_str))
            l_str = str(self.get_key(l) if l < n else None)
            l_str = l_str+' '*(6-len(l_str))
            r_str = str(self.get_key(r) if r < n else None)
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
