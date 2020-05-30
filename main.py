'''Given a name, it returns his/her birth day, death, homwtown an
name of the people born in the same century, according to different
level of verbosity'''

import argparse
import csv
import sqlite3
import hashlib
import random
import sys
import logging
import verboselogs
from birthdays_package.birthdays_module import (
    return_data, return_index, return_set)


conn = None
cursor = None
dbpath = 'scripts/mydatabase.db'

logging.basicConfig(level=logging.INFO)
verboselogs.install()
logger = logging.getLogger('main_logger')


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
    global logger

    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    salt = cursor.execute(
        "SELECT salt FROM user WHERE username=?", (username,))
    salt = salt.fetchall()
    if salt == []:
        logger.error('Invalid Username!\nPlease, Check Your Username...')
        logger.verbose('See README on how to create a new user!')
        logger.spam('Run dbmanager.py -a username -p password to add new user')
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
        logger.info('Username Correct! Password Correct!')
        logger.info('You are allowed to access the program!\n')
        logger.verbose('Please see README or use -h for advanced options!')
    else:
        logger.error('Invalid Password! \nPlease, Check Your Password...')
        logger.spam('Use dbmanager.py to change user\'s password.')
        quit()
    conn.commit()


def parse_arguments():
    '''Define arguments that the user will input and that will be
    parsed through'''
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="return the birthday", type=str)
    parser.add_argument("-v", "--verbosity", help="increase output verbosity",
                        action="count")
    parser.add_argument("-u", "--set", help="group the birthdays",
                        action="store_true")
    parser.add_argument('-c', help="check for a usernamename", required=True)
    parser.add_argument('-p', help="the username password", required=True)

    args = parser.parse_args()
    
    if args.verbosity:
        if args.verbosity >= 2:
            logger.setLevel(logging.SPAM)
        elif args.verbosity == 1:
            logger.setLevel(logging.VERBOSE)
        
    if args.set:
        dt_same = return_set(args.name)
        for item in dt_same:
            logger.info(item+": " + dt_same[item])
        
    i = return_index(args.name)
    dataset = return_data()
    
    if i == None:
        logger.error('error\nPerson not found!')
        logger.spam('Please see birthdays.csv file to add new information.' )
    else:
        name = args.name.upper()
        if args.c and args.p:
            check_for_user(args.c, args.p)
            
        logger.info(name + '\'s' + ' birthday is: ' + dataset[1][i])
        logger.verbose(name + '\'s' + ' death is: ' + dataset[2][i])
        logger.spam(name + '\'s' + ' city is: ' + dataset[3][i])


if __name__ == "__main__":
    args = parse_arguments()

conn.close()
