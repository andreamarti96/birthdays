'''
Return the birthday of a given person
'''

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}


def print_birthdays():
    '''Print all the names of the people in the birthdays dictionaries'''
    print('Welcome to the birthday dictionary. \
We know the birthdays of these people:')
    for name in birthdays:
        print(name)


def return_birthday(name):
    '''If the name is in the birthdays dictionaries \
print the birthday otherwise print a warning message'''
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))
