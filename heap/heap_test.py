import unittest
from heap import Heap

class TestHeap(unittest.TestCase):

    # --- 1. Creation Tests ---
    
    def test_min_heap_creation(self):
        nodes = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        min_heap = Heap(order_criteria='min', nodes=nodes)
        self.assertEqual(min_heap.peek(), 1, "Root of min-heap should be the smallest element")

    def test_max_heap_creation(self):
        nodes = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        max_heap = Heap(order_criteria='max', nodes=nodes)
        self.assertEqual(max_heap.peek(), 9, "Root of max-heap should be the largest element")

    def test_tuple_heap_creation(self):
        nodes = [(3, 'C'), (1, 'A'), (2, 'B')]
        tuple_heap = Heap(order_criteria='min', nodes=nodes)
        self.assertEqual(tuple_heap.peek(), (1, 'A'), "Root should be the tuple with the smallest first element")

    # --- 2. Peek Tests ---

    def test_peek_empty_heap(self):
        empty_heap = Heap(order_criteria='min', nodes=[])
        self.assertIsNone(empty_heap.peek(), "Peeking an empty heap should return None")

    def test_peek_does_not_remove(self):
        h = Heap(order_criteria='max', nodes=[10, 20, 5])
        initial_length = len(h.nodes)
        h.peek()
        self.assertEqual(len(h.nodes), initial_length, "Peek should not alter the size of the heap")

    # --- 3. Insert Tests ---

    def test_insert_min_heap(self):
        h = Heap(order_criteria='min', nodes=[5, 10, 15])
        h.insert(2) # Should become the new root
        self.assertEqual(h.peek(), 2, "Inserted smallest element should bubble up to root")
        
    def test_insert_max_heap(self):
        h = Heap(order_criteria='max', nodes=[10, 5, 2])
        h.insert(20) # Should become the new root
        self.assertEqual(h.peek(), 20, "Inserted largest element should bubble up to root")

    def test_insert_type_validation(self):
        h = Heap(order_criteria='min', nodes=[1.0, 2.0])
        with self.assertRaises(ValueError):
            h.insert((3.0, "Invalid because base is float, not tuple"))
            
        h_tuple = Heap(order_criteria='min', nodes=[(1, 'A')])
        with self.assertRaises(ValueError):
            h_tuple.insert(('String', 'Invalid first element'))

    # --- 4. Pop Tests ---

    def test_pop_min_heap_order(self):
        h = Heap(order_criteria='min', nodes=[3, 1, 4, 1, 5, 9])
        popped_elements = []
        while not h._is_empty():
            popped_elements.append(h.pop())
        
        expected_order = [1, 1, 3, 4, 5, 9]
        self.assertEqual(popped_elements, expected_order, "Min-heap should pop elements in ascending order")

    def test_pop_max_heap_order(self):
        h = Heap(order_criteria='max', nodes=[3, 1, 4, 1, 5, 9])
        popped_elements = []
        while not h._is_empty():
            popped_elements.append(h.pop())
        
        expected_order = [9, 5, 4, 3, 1, 1]
        self.assertEqual(popped_elements, expected_order, "Max-heap should pop elements in descending order")

    def test_pop_empty_heap(self):
        h = Heap(order_criteria='min', nodes=[])
        self.assertIsNone(h.pop(), "Popping from an empty heap should return None")

    def test_pop_single_element(self):
        h = Heap(order_criteria='min', nodes=[42])
        self.assertEqual(h.pop(), 42)
        self.assertIsNone(h.peek(), "Heap should be empty after popping the only element")

if __name__ == '__main__':
    unittest.main()