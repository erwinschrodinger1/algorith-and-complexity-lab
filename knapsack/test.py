from knapsack import bruteforce, greedy, dynamic
import unittest


class TestKnapsackMethods(unittest.TestCase):

    def test_empty_case(self):
        input_value = []
        input_capacity = 10
        expected_output = []

        bruteforce_output = bruteforce(input_value, input_capacity)
        self.assertEqual(expected_output, bruteforce_output)

        greedy_output = greedy(input_value, input_capacity)
        self.assertEqual(expected_output, greedy_output)

        dynamic_output = dynamic(input_value, input_capacity)
        self.assertEqual(expected_output, dynamic_output)

    def test_single_item_fits(self):
        input_value = [{"weight": 1, "profit": 2}]
        input_capacity = 5
        expected_output = [{"weight": 1, "profit": 2}]

        bruteforce_output = bruteforce(input_value, input_capacity)
        self.assertEqual(expected_output, bruteforce_output)

        greedy_output = greedy(input_value, input_capacity)
        self.assertEqual(expected_output, greedy_output)

        dynamic_output = dynamic(input_value, input_capacity)
        self.assertEqual(expected_output, dynamic_output)

    def test_single_item_does_not_fit(self):
        input_value = [{"weight": 10, "profit": 20}]
        input_capacity = 5
        expected_output_10 = []

        expected_output_fraction = [
            {"weight": 5, "profit": 10},
        ]

        bruteforce_output = bruteforce(input_value, input_capacity)
        self.assertEqual(expected_output_10, bruteforce_output)

        greedy_output = greedy(input_value, input_capacity)
        self.assertEqual(expected_output_fraction, greedy_output)

        dynamic_output = dynamic(input_value, input_capacity)
        self.assertEqual(expected_output_10, dynamic_output)

    def test_random_case(self):
        input_value = [
            {"weight": 10, "profit": 20},
            {"weight": 20, "profit": 10},
            {"weight": 30, "profit": 50},
        ]
        input_capacity = 40

        expected_output_10 = [
            {"weight": 10, "profit": 20},
            {"weight": 30, "profit": 50},
        ]

        bruteforce_output = bruteforce(input_value, input_capacity)
        self.assertEqual(expected_output_10, bruteforce_output)

        expected_output_fraction = [
            {"weight": 10, "profit": 20},
            {"weight": 30, "profit": 50},
        ]

        greedy_output = greedy(input_value, input_capacity)
        self.assertEqual(expected_output_fraction, greedy_output)

        dynamic_output = dynamic(input_value, input_capacity)
        self.assertEqual(expected_output_10, dynamic_output)


if __name__ == "__main__":
    unittest.main()
