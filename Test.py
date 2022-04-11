from unittest import mock
from unittest import TestCase
from main import *


class TestingSolvingAlgorithms(TestCase):
    @mock.patch('main.input', create=True)
    def testBruteForce(self, mocked_input):
        mocked_input.side_effect = [4, 5, 1, 1]
        test_case_one = BruteForce(2, 4).solution()
        mocked_input.side_effect = [4, 5, 1, 1]
        self.assertEqual(test_case_one, 1)
        mocked_input.side_effect = [2, 3, 4, 5, 1, 2, 5, 6]
        test_case_two = BruteForce(4, 8).solution()
        self.assertEqual(test_case_two, 8)
        print("All tests were passed for Bruteforce solution were passed")

    @mock.patch('main.input', create=True)
    def testDp(self, mocked_input):
        mocked_input.side_effect = [4, 5, 1, 1]
        test_case_one = DynamicProgramming(2, 4).solution()
        self.assertEqual(test_case_one, 1)
        mocked_input.side_effect = [2, 3, 4, 5, 1, 2, 5, 6]
        test_case_two = DynamicProgramming(4, 8).solution()
        self.assertEqual(test_case_two, 8)
        print("All tests were passed for DP solution were passed")

    @mock.patch('main.input', create=True)
    def testGreedy(self, mocked_input):
        mocked_input.side_effect = [4, 5, 1, 1]
        test_case_one = GreedySolution(2, 4).solution()
        self.assertEqual(test_case_one, 1)
        mocked_input.side_effect = [2, 3, 4, 5, 1, 2, 5, 6]
        test_case_two = GreedySolution(4, 8).solution()
        self.assertEqual(test_case_two, 9.8)
        mocked_input.side_effect = [2, 3, 5, 7, 1, 4, 1, 10, 5, 15, 7, 6, 18, 3]
        test_case_two = GreedySolution(7, 15).solution()
        self.assertEqual(round(test_case_two, 1), 55.3)
        print("All tests were passed for Greedy solution were passed")
