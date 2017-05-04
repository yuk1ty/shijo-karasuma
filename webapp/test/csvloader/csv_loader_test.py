import sys
sys.path.append('../')
import unittest

from csvloader import *

class CsvLoaderTest(unittest.TestCase):

    def test_load(self):
        loader = CsvLoader()
        loader.load("data/test.csv")

        self.assertEqual(true, true)

if __name__ == "__main__":
    unittest.main()
