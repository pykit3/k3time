import doctest
import unittest

import k3time


class TestDoctest(unittest.TestCase):
    def test_doctest(self):
        # pytest does not call the unittest load_tests hook, so a test method runs the examples.
        result = doctest.testmod(k3time)
        self.assertEqual(doctest.TestResults(failed=0, attempted=3), result)
