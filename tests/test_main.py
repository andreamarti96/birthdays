"""Test code to check for errors."""

import unittest
import os
from birthdays_package.birthdays_module import return_data
from birthdays_package.birthdays_module import return_index
from birthdays_package.birthdays_module import return_set


class TestMain(unittest.TestCase):

    def setUp(self):
        self.temporary_file = "/tmp/temporary_file.csv"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        """Check if there is a csv file."""
        data = return_data(filename='/tmp/random_file.csv')
        self.assertFalse(data)


    def tearDown(self):
        os.remove(self.temporary_file)


if __name__ == '__main__':
    unittest.main()
