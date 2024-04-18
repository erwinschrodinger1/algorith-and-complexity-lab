import unittest
from lab1.insertion_sort import insertion_sort
from lab1.selection_sort import selection_sort

class Test_Sorting(unittest.TestCase):
    def test_sort_random(self):
        input_data = [1,2,32,12,321,1]
        result_insertion = insertion_sort(input_data)
        result_selection = selection_sort(input_data)
        self.assertEqual(result_insertion,[1,1,2,12,32,321], )
        self.assertEqual(result_insertion,result_selection, )
        
    def test_sort_empty(self):
        input_data = []
        result_insertion = insertion_sort(input_data)
        result_selection = selection_sort(input_data)
        self.assertEqual(result_insertion,[], )
        self.assertEqual(result_insertion,result_selection, )

    def test_sort_best(self):
        input_data = [1,2,3,4,5]
        result_insertion = insertion_sort(input_data)
        result_selection = selection_sort(input_data)
        self.assertEqual(result_insertion,[1,2,3,4,5], )
        self.assertEqual(result_insertion,result_selection, )
        
    def test_sort_worst(self):
        input_data = [5,4,3,2,1]
        result_insertion = insertion_sort(input_data)
        result_selection = selection_sort(input_data)
        self.assertEqual(result_insertion,[1,2,3,4,5], )
        self.assertEqual(result_insertion,result_selection, )


if __name__=="__main__":
    unittest.main()