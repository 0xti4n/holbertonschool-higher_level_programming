#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_nomal_list(self):
        li = [1, 2, 3, 4]
        self.assertEqual(max_integer(li), 4)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            li = [1, 3, "hola", 4]
            max_integer(li)		           

    def test_with_negative(self):
        li = [1, 2, 3, -4]
        self.assertEqual(max_integer(li), 3)

    def empty_list(self):
        li = []
        self.assertIsNone(max_integer(li))
