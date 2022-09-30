import unittest
from util.heap import *


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = []

    def test_heappush(self):
        heappush(self.heap, 5)
        heappush(self.heap, 4)
        heappush(self.heap, 1)
        heappush(self.heap, 3)
        #   1
        #  3 4
        # 5
        self.assertEqual(self.heap[0], 1)
        self.assertEqual(self.heap[1], 3)
        self.assertEqual(self.heap[2], 4)
        self.assertEqual(self.heap[3], 5)

        heappush(self.heap, 1)
        #   1
        #  1 4
        # 5 3
        self.assertEqual(self.heap[0], 1)
        self.assertEqual(self.heap[1], 1)
        self.assertEqual(self.heap[2], 4)
        self.assertEqual(self.heap[3], 5)
        self.assertEqual(self.heap[4], 3)

        heappush(self.heap, 10)
        heappush(self.heap, 1)
        #    1
        #  1   1
        # 5 3 10 4
        self.assertEqual(self.heap[0], 1)
        self.assertEqual(self.heap[1], 1)
        self.assertEqual(self.heap[2], 1)
        self.assertEqual(self.heap[3], 5)
        self.assertEqual(self.heap[4], 3)
        self.assertEqual(self.heap[5], 10)
        self.assertEqual(self.heap[6], 4)

    def test_heappop(self):
        heappush(self.heap, 1)
        heappush(self.heap, 1)
        heappush(self.heap, 1)
        heappush(self.heap, 5)
        heappush(self.heap, 3)
        heappush(self.heap, 10)
        heappush(self.heap, 4)
        #    1
        #  1   1
        # 5 3 10 4

        heappop(self.heap)
        #    1
        #  1   4
        # 5 3 10
        self.assertEqual(self.heap[0], 1)
        self.assertEqual(self.heap[1], 1)
        self.assertEqual(self.heap[2], 4)
        self.assertEqual(self.heap[3], 5)
        self.assertEqual(self.heap[4], 3)
        self.assertEqual(self.heap[5], 10)

        heappop(self.heap)
        #    1
        #  3   4
        # 5 10
        self.assertEqual(self.heap[0], 1)
        self.assertEqual(self.heap[1], 3)
        self.assertEqual(self.heap[2], 4)
        self.assertEqual(self.heap[3], 5)
        self.assertEqual(self.heap[4], 10)

    def test_down(self):
        self.heap.append(2)
        self.heap.append(3)
        self.heap.append(4)
        self.heap.append(5)
        self.heap.append(10)
        self.heap.append(1)
        #     2
        #  3    4
        # 5 10 1

        # Start position = 2, so only until 2 index
        # Basically in this case should only swap 1 and 4
        down(self.heap, 2, len(self.heap) - 1)
        #     2
        #  3    1
        # 5 10 4
        self.assertEqual(self.heap[0], 2)
        self.assertEqual(self.heap[1], 3)
        self.assertEqual(self.heap[2], 1)
        self.assertEqual(self.heap[3], 5)
        self.assertEqual(self.heap[4], 10)
        self.assertEqual(self.heap[5], 4)

