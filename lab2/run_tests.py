import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('.'))

test_loader = unittest.TestLoader()
test_suite = test_loader.discover('tests', pattern='test_*.py')

test_runner = unittest.TextTestRunner(verbosity=2)
result = test_runner.run(test_suite)

sys.exit(not result.wasSuccessful())