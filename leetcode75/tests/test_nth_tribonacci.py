from unittest import TestCase
from leetcode75.dp_1d.nth_tribonacci import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_tribonacci(self):
        n = 4
        self.assertEqual(self.sol.tribonacci(n), 4)

        n = 25
        self.assertEqual(self.sol.tribonacci(n), 1389537)

    def test_tribonacci_iterative(self):
        n = 4
        self.assertEqual(self.sol.tribonacci_iterative(n), 4)

        n = 25
        self.assertEqual(self.sol.tribonacci_iterative(n), 1389537)
