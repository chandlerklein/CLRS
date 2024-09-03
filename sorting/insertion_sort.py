import unittest
from typing import List


def insertion_sort(arr: List[int]) -> None:
    if not arr or len(arr) < 2:
        return
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


class InsertionSortTest(unittest.TestCase):
    def test_none_list(self):
        insertion_sort(None)

    def test_empty_list(self):
        arr = []
        insertion_sort(arr)
        self.assertListEqual(arr, [])

    def test_one_element_list(self):
        arr = [3]
        insertion_sort(arr)
        self.assertListEqual(arr, [3])

    def test_two_element_list(self):
        arr = [3, -1]
        insertion_sort(arr)
        self.assertListEqual(arr, [-1, 3])

    def test_sort(self):
        arr = [3, 1, 9, 3, -2, 11, 3, 20, 6]
        insertion_sort(arr)
        self.assertListEqual(arr, [-2, 1, 3, 3, 3, 6, 9, 11, 20])


if __name__ == '__main__':
    unittest.main()
