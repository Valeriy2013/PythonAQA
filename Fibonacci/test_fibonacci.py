"""
Unit tests for the fibonacci library
"""

import fibonacci
import pytest
import random


@pytest.mark.fibonacci
class TestFibonacci:

    def test_generateFibonacci(self):
        assert [1, 1, 2, 3, 5, 8, 13] == fibonacci.generateFibonacci(7), "Check fibonacci sequence"

    @pytest.mark.flaky(reruns=5)
    def test_randomNumber(self):
        num = random.randint(1, 2)
        assert num == 2, "Check random number"
