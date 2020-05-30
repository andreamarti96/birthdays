'''
This is our birthday module.
'''


import csv


def return_data(filename='birthdays_package/birthdays.csv'):
    ''' Open the birthdays.csv and return name, date of birth, date of death
    (if exists) and city.
    
    :param filename: (str) The path the file that contains the data
    :return: data about the chosen person (name, birth, death, city)
    '''
    arr_name = []
    arr_birth = []
    arr_death = []
    arr_city = []
    try:
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                arr_name += [row[0]]
                arr_birth += [row[1]]
                arr_death += [row[2]]
                arr_city += [row[3]]
        return arr_name, arr_birth, arr_death, arr_city
    except FileNotFoundError:
        return False


data_s = return_data()


def return_index(name):
    ''' Open the birthdays.csv and return name, date of birth, date of death
    (if exists) and city.
    
    :param filename: (str) The path the file that contains the data
    :return: data about the chosen person (name, birth, death, city)
    '''
    count = -1
    for i in data_s[0]:
        count += 1
        if name == i:
            return count
    return None


def return_set(name):
    ''' Return the name of the persons born in the same century of the one that
    the user is trying to search for.
    
    :param name: (str) the name of the person to base the search on
    :return dt_same: (dict) dictionary containing people born in the same ct.
    '''
    set_b = data_s[1]
    set_n = data_s[0]
    set_same_b = []
    set_same_n = []
    set_b.pop(0)
    set_n.pop(0)
    dt = dict(zip(set_n, set_b))
    for i in set_b:
        if i[-3] == data_s[1][return_index(name)][-3]:
            set_same_b += [i]
    for key in dt:
        if dt[key] in set_same_b:
            set_same_n += [key]
    dt_same = dict(zip(set_same_n, set_same_b))
    return dt_same
