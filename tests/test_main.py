"""Test code to check for errors."""

import unittest
from birthdays_package.test import csv_reader
from birthdays_package.test import type_f
import sys
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        self.temporary_file = "/tmp/temporary_file.csv"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        """Check if there is a csv file."""
        self.assertFalse(os.path.exists("birthdays_package/random_name.csv"))

    def test_empty_datafile(self):
        """Check the presence of data inside the csv file."""
        datafile = csv_reader(path=self.temporary_file)
        self.assertFalse(datafile)

    def test_valid_extension(self):
        """Check the extension of the file."""
        extension = type_f(path=self.temporary_file)
        self.assertEqual(extension, ".csv")

    def tearDown(self):
        os.remove(self.temporary_file)


if __name__ == '__main__':
    unittest.main()
