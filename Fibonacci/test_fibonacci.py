"""
Unit tests for the fibonacci library
"""

import fibonacci
import pytest


class TestFibonacci:

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_generateFibonacci(self):
        assert [1, 1, 2, 3, 5, 8, 13] == fibonacci.generateFibonacci(7)
