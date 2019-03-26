import time
import unittest

import pytest

pytest.skip("This does not generate code coverage", allow_module_level=True)


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        # A long time ago in a galaxy far, far away...
        time.sleep(2)

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_upper_bar(self):
        self.assertEqual("foo".upper(), "BAR")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
