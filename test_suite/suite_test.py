from test_case import test
import unittest


def test_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(test.TestTest))
    return suite
