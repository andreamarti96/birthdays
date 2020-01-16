"""Test the creation of csv."""

import csv
import os.path


def type_f(path):
    """Find the extention of the file."""
    extension = os.path.splitext(path)[1]
    return extension


def csv_reader(path):
    """Read csv file."""
    arr_name = []
    arr_birth = []
    arr_death = []
    arr_city = []
    with open(path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            arr_name += [row[0]]
            arr_birth += [row[1]]
            arr_death += [row[2]]
            arr_city += [row[3]]


csv_reader('birthdays_package/birthdays.csv')

