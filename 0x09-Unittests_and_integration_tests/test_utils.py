#!/usr/bin/env python3
"""
parameterize a unit test
"""
import unittest
from parameterized import parameterized
from typing import Any


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1), 
        ({"a": {"b": 2}}, ("a",), {"b": 2}), 
        ({"a": {"b": 2}}, ("a", "b"), 2), 
        ])
    def test_access_nested_map(self) -> Any:
        """
        method to test method access_nested_map in utils.py
        """
        self.assertEqual()
