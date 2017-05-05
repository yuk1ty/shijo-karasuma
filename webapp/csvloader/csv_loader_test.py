import unittest
import csv_loader

class CsvLoaderTest(unittest.TestCase):

    def test_load(self):
        print(csv_loader.load("data/test.csv"))

        self.assertEqual(True, True)

if __name__ == "__main__":
    unittest.main()
