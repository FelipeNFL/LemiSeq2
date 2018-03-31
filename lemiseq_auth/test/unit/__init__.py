import unittest
import sys
import logging


if __name__ == '__main__':

    logging.disable(logging.CRITICAL)

    loader = unittest.TestLoader()
    big_suite = loader.discover(".", "Test*.py")
    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
    sys.exit(not results.wasSuccessful())
