from typing import Generic, TypeVar, Any

real = int | float  # Allowed data type of keys in heap
# Type definition valid for Python 3.11 or newer
T = TypeVar('T', bound=real | tuple[real, *tuple[Any, ...]]) # Heaps store real values or tuples where a real value is first element

class Heap(Generic[T]):
    """
    Heap class

    Creates a heap from an array of nodes
    """

    def __init__(self, order_criteria: str,
                 nodes: list[T]):
        """
        Constructor method

        Parameters
        __________
        order_criteria : str
            An string value among 'min' for Min-heap and 'max' for Max-heap
        nodes : list[real] or list[tuple]
            A list of numbers or tuples. In case of tuples first
            value of each tuple must a number
        """
        self.nodes = nodes
        if order_criteria == 'max':
            self._heap_op = self._greater_than
            self.type = 'Max-heap'
        elif order_criteria == 'min':
            self._heap_op = self._less_than
            self.type = 'Min-heap'
        for idx_parent in range(len(nodes)//2-1, -1, -1):
            self._bubble_down(idx_parent)

    @staticmethod
    def _less_than(left: real, right: real) -> bool:
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
    def _greater_than(left: real, right: real) -> bool:
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
    def _parent(idx: int) -> int:
        """
        Finds the parent node index of a given child node index

        Parameters
        ----------
        idx: int
            Index of child node

        Returns
        -------
        int
            Index of parent node index
        """
        return (idx-1)//2

    @staticmethod
    def _left(idx: int) -> int:
        """
        Finds the left child node index of a given parent node index

        Parameters
        ----------
        idx: int
            Index of parent node

        Returns
        -------
        int
            Index of left child node index
        """
        return 2 * idx + 1

    @staticmethod
    def _right(idx: int) -> int:
        """
        Finds the right child node index of a given parent node index

        Parameters
        ----------
        idx: int
            Index of parent node

        Returns
        -------
        int
            Index of right child node index
        """
        return 2 * idx + 2

    @staticmethod
    def _check_retrieve_key(node: T) -> real:
        """
        Checks that `node` is of instance real or tuple[real, ...] and returns the real key

        Parameters
        ----------
        node : real, tuple[real, ...]
            Element of heap

        Returns
        -------
        real
            Value of node or None if value can't be retrieved
        """
        if isinstance(node, real):
            return node
        elif isinstance(node, tuple):
            if isinstance(node[0], real):
                return node[0]
            else:
                raise ValueError("First element of tuple must be a real number")
        else:
            raise ValueError("Node element must be a real value or tuple with first element a real value")

    def _is_empty(self) -> bool:
        """
        Indicates whether the heap is empty or not

        Returns
        -------
        bool
            True when heap is empty, False otherwise
        """
        return len(self.nodes) == 0


    def _get_key(self, idx: int) -> real:
        """
        Gets key at `index` node

        Parameters
        ----------
        idx : int
            index of the node to retrieve the key from

        Returns
        -------
        int
            Returns key of node at `idx`.
        """
        if idx < 0 or idx >= len(self.nodes):
            raise IndexError('Index is out of bounds for heap size')
        key = self._check_retrieve_key(self.nodes[idx])
        return key

    def _bubble_up(self, idx: int) -> None:
        """
        Bubbles up element from node at index `idx` towards the root

        Parameters
        ----------
        idx : int
            Index of node to bubble up towards the root
        """
        idx_child = idx
        child = self.nodes[idx_child]
        idx_p = self._parent(idx_child)
        while idx_child>0 and (self._heap_op(self._get_key(idx_child), self._get_key(idx_p))):
            self.nodes[idx_child] = self.nodes[idx_p]
            self.nodes[idx_p] = child
            idx_child = idx_p
            idx_p = self._parent(idx_child)

    def _bubble_down(self, idx_parent: int) -> None:
        """
        Bubbles down element from node at index `idx` towards the leaves

        Parameters
        ----------
        idx : int
            Index of node to bubble down towards the leaves
        """
        n = len(self.nodes)
        idx_l = self._left(idx_parent)
        idx_r = self._right(idx_parent)
        idx_child = idx_parent
        if idx_l < n and self._heap_op(self._get_key(idx_l),
                                    self._get_key(idx_child)):
            idx_child = idx_l
        if idx_r < n and self._heap_op(self._get_key(idx_r),
                                    self._get_key(idx_child)):
            idx_child = idx_r
        if idx_child == idx_parent:
            return None
        else:
            tmp = self.nodes[idx_parent]
            self.nodes[idx_parent] = self.nodes[idx_child]
            self.nodes[idx_child] = tmp
            self._bubble_down(idx_child)

    def peek(self) -> T | None:
        """
        Peek the heap to find value at the root

        Returns
        -------
        int, tuple[int, ...]
            Return number or tuple, as first value at root of heap
        """
        if self._is_empty():
            return None
        else:
            return self.nodes[0]

    def insert(self, node: T) -> None:
        """
        Inserts node in heap while maintaining the heap rule intact

        Parameters
        ----------
        node : real, tuple[real, ...]
            Value to be inserted in the heap. It needs to be of the same
            type of values already contained in the heap
        """
        if self._is_empty(): 
            self.nodes.append(node)
        elif isinstance(node, real if isinstance(self.nodes[0], real) else tuple):
            if isinstance(node, tuple):
                if not isinstance(node[0], real):
                    raise ValueError("First item of tuple is not a real value")
            self.nodes.append(node)
            idx = len(self.nodes)-1
            self._bubble_up(idx)
        else:
            raise ValueError(f'New item must be of the same type of nodes in the heap: {type(self.nodes[0])}')

    def pop(self) -> T | None:
        """
        Pops min or max node from the heap and returns its value

        Parameters
        ----------

        Returns
        -------
        real, tuple[real, ...]
            Return the item removed at `index`, be a real number or a tuple
            where the first value is a real number
        """
        n = len(self.nodes)

        if n == 0:
            return None

        item = self.nodes.pop()
        if n-1 == 0:
            return item
        min_max_item = self.nodes[0]
        self.nodes[0] = item
        self._bubble_down(0)
        return min_max_item

if __name__=="__main__":
    pass