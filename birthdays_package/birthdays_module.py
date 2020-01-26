"""This is our birthday module."""


import csv


'''Open the birthdays.csv and return data'''


def return_data(filename='birthdays_package/birthdays.csv'):
    arr_name = []
    arr_birth = []
    arr_death = []
    arr_city = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            arr_name += [row[0]]
            arr_birth += [row[1]]
            arr_death += [row[2]]
            arr_city += [row[3]]
    return arr_name, arr_birth, arr_death, arr_city


data_s = return_data()

'''Return the index of the typed name'''


def return_index(name):
    count = -1
    for i in data_s[0]:
        count += 1
        if name == i:
            return count


'''Return the name of the persons born in the same century'''


def return_set(name):
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
    print("People born in the same century of " + name.upper() + ":")
    for item in dt_same:
        print(item+": " + dt_same[item])
