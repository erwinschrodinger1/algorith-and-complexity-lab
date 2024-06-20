from lab2.merge_sort import merge_sort
from lab2.quick_sort import quick_sort
from lab1.insertion_sort import insertion_sort
from lab1.selection_sort import selection_sort
import unittest


class TestSorting(unittest.TestCase):
    def test_sort_random(self):
        input_data = [1, 2, 32, 12, 321, 1]
        expected = [1, 1, 2, 12, 32, 321]

        result_insertion = insertion_sort(input_data.copy())
        result_selection = selection_sort(input_data.copy())
        result_quick = input_data.copy()
        quick_sort(result_quick, 0, len(input_data) - 1)
        result_merge = input_data.copy()
        merge_sort(result_merge, 0, len(input_data) - 1)

        self.assertEqual(result_insertion, expected)
        self.assertEqual(result_selection, expected)
        self.assertEqual(result_quick, expected)
        self.assertEqual(result_merge, expected)

    def test_sort_empty(self):
        input_data = []
        expected = []

        result_insertion = insertion_sort(input_data.copy())
        result_selection = selection_sort(input_data.copy())
        result_quick = input_data.copy()
        quick_sort(result_quick, 0, len(input_data) - 1)
        result_merge = input_data.copy()
        merge_sort(result_merge, 0, len(input_data) - 1)

        self.assertEqual(result_insertion, expected)
        self.assertEqual(result_selection, expected)
        self.assertEqual(result_quick, expected)
        self.assertEqual(result_merge, expected)

    def test_sort_best(self):
        input_data = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]

        result_insertion = insertion_sort(input_data.copy())
        result_selection = selection_sort(input_data.copy())
        result_quick = input_data.copy()
        quick_sort(result_quick, 0, len(input_data) - 1)
        result_merge = input_data.copy()
        merge_sort(result_merge, 0, len(input_data) - 1)

        self.assertEqual(result_insertion, expected)
        self.assertEqual(result_selection, expected)
        self.assertEqual(result_quick, expected)
        self.assertEqual(result_merge, expected)

    def test_sort_worst(self):
        input_data = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]

        result_insertion = insertion_sort(input_data.copy())
        result_selection = selection_sort(input_data.copy())
        result_quick = input_data.copy()
        quick_sort(result_quick, 0, len(input_data) - 1)
        result_merge = input_data.copy()
        merge_sort(result_merge, 0, len(input_data) - 1)

        self.assertEqual(result_insertion, expected)
        self.assertEqual(result_selection, expected)
        self.assertEqual(result_quick, expected)
        self.assertEqual(result_merge, expected)


if __name__ == "__main__":
    unittest.main()
