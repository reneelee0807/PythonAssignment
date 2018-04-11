from test.unit_test_filer import FilerUnitTest
import doctest
import unittest


def doc_tests():
    doctest.testfile("test/doc_test_filer.txt", verbose=1)
    doctest.testfile("test/doc_test_validator.txt", verbose=1)


def unit_tests():
    the_suite = unittest.TestSuite()

    the_suite.addTest(unittest.makeSuite(FilerUnitTest))
    # the_suite.addTest(unittest.makeSuite(FilerTests))
    # the_suite.addTest(unittest.makeSuite(ControllerTests))

    return the_suite


if __name__ == "__main__":
    doc_tests()
    runner = unittest.TextTestRunner(verbosity=2)

    test_suite = unit_tests()
    runner.run(test_suite)