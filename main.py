import argparse
import csv
import sqlite3
import hashlib
import random
import sys
from birthdays_package.birthdays_module import (return_data,
return_index, return_set)


conn = None
cursor = None
dbpath = 'scripts/mydatabase.db'


def open_and_create():
    '''Check if database exists in a specific file, if not create one.'''
    global conn
    global cursor
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
    except sqlite3.OperationalError:
        dbmanager.save_new_user(conn, cursor)


def check_for_user(username, password):
    '''Check if database exists in a specific file'''
    global conn
    global cursor
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    salt = cursor.execute(
        "SELECT salt FROM user WHERE username=?", (username,))
    salt = salt.fetchall()
    if salt == []:
        print('Invalid Username')
        print('Please, Check Your Username...')
        quit()
    salt = salt[0][0]
    results = cursor.execute(
        "SELECT digest FROM user WHERE username=?", (username,))
    results = results.fetchall()[0][0]
    digest = salt + password
    for i in range(1000000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    conn.commit()
    if digest == results:
        print('Username Correct')
        print('Password Correct')
        print('You are allowed to access the program!')
    else:
        print("Invalid Password")
        print('Please, Check Your Password...')
        quit()
    conn.commit()


'''Given a name, it returns his/her birth day, death, homwtown an
name of the people born in the same century, according to different
level of verbosity'''


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="return the birthday", type=str)
    parser.add_argument("-v", "--verbosity", help="increase output verbosity",
                        action="count")
    parser.add_argument("-u", "--set", help="group the birthdays",
                        action="store_true")
    parser.add_argument('-c', help="check for a usernamename", required=True)
    parser.add_argument('-p', help="the username password", required=True)

    args = parser.parse_args()
    i = return_index(args.name)
    dataset = return_data()
    if i is None:
        print("error")
    else:
        if args.c and args.p:
            check_for_user(args.c, args.p)
        if args.verbosity > 1:
            print('The '+args.name.upper() + '\'s' + ' birthday is: ' +
                  dataset[1][i])
            print('The '+args.name.upper() + '\'s' + ' death is: ' +
                  dataset[2][i])
            print('The '+args.name.upper() + '\'s' + ' hometown is: ' +
                  dataset[3][i])
        elif args.verbosity == 1:
            print('The ' + args.name.upper() + '\'s' + ' birthday is: ' +
                  dataset[1][i])
            print('The ' + args.name.upper() + '\'s' + ' death is: ' +
                  dataset[2][i])
        elif args.set:
            return_set(args.name)
        else:
            print('The '+args.name.upper() + '\'s' + ' birthday is: ' +
                  dataset[1][i])

if __name__ == "__main__":
    args = parse_arguments()

conn.close()

