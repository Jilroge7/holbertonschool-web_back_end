#!/usr/bin/env python3
"""
playing with parameterize, mock
on utility methods
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
import requests
import json
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test class for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        method to test expected res in method access_nested_map in utils.py
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        method to test for exceptions in access_nested_map
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unit test class for utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_request):
        """
        method to test expected res in get_json method
        """
        mock_request().json.return_value = test_payload
        mock_request.assert_called_once()
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Unit test class for memoize
    """
    def test_memoize(self):
        """
        method to test functionality of memoize decorator
        """
        class TestClass:
            """
            Test class for test memoize
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_a_:
            test = TestClass()
            test_call_one = test.a_property
            test_call_two = test.a_property
            self.assertEqual(test_call_one, 42)
            self.assertEqual(test_call_two, 42)

            mock_a_.assert_called_once()
