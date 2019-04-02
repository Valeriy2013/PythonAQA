"""
Unit tests for the fibonacci library
"""

import fibonacci


class TestFibonacci:

    def test_generateFibonacci(self):
        assert [1, 1, 2, 3, 5, 8, 13] == fibonacci.generateFibonacci(7)
