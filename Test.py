from unittest import TestCase
from main import *

class TestingSolvingAlgorithms(TestCase):

    def testBruteForce(self):
        weights = [4, 5]
        profits = [1, 1]
        test_case_one = BruteForce(2, 4, weights, profits).solution()
        self.assertEqual(test_case_one, 1)
        weights = [2, 3, 4, 5]
        profits = [1, 2, 5, 6]
        test_case_two = BruteForce(4, 8, weights, profits).solution()
        self.assertEqual(test_case_two, 8)

    def testDp(self):
        weights = [4, 5]
        profits = [1, 1]
        test_case_one = DynamicProgramming(2, 4, weights, profits).solution()
        self.assertEqual(test_case_one, 1)
        weights = [2, 3, 4, 5]
        profits = [1, 2, 5, 6]
        test_case_two = DynamicProgramming(4, 8, weights, profits).solution()
        self.assertEqual(test_case_two, 8)        

    def testGreedy(self, ):
        weights = [4, 5]
        profits = [1, 1]
        test_case_one = GreedySolution(2, 4, weights, profits).solution()
        self.assertEqual(test_case_one, 1)
        weights = [2, 3, 4, 5]
        profits = [1, 2, 5, 6]
        test_case_two = GreedySolution(4, 8, weights, profits).solution()
        self.assertEqual(test_case_two, 9.8)
        weights = [2, 3, 5, 7, 1, 4, 1]
        profits = [10, 5, 15, 7, 6, 18, 3]
        test_case_two = GreedySolution(7, 15, weights, profits).solution()
        self.assertEqual(round(test_case_two, 1), 55.3)
        
