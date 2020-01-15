import sqlite3
import hashlib
import random
import argparse

conn = None
cursor = None

''' Creating tables named user and columns like:
username, digest, and salt. The primary key is
assigned to digest.'''


def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE user
                      (username CHAR(256),
                       digest CHAR(256),
                       salt CHAR(256),
                       PRIMARY KEY (digest))''')

''' Creating new optional argumnets for adding the user with his/her password

'''


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    return parser.parse_args()

''' Adding new user and password to database user'''


def save_new_username(username, password):
    global conn
    global cursor
    salt = str(random.random())
    digest = salt + password
    for i in range(1000000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, digest, salt))
    conn.commit()
    print ("User {} succesfully added to data.db".format(username))


open_and_create()
args = parse_args()

if args.a and args.p:
    save_new_username(args.a, args.p)
else:
    print ("Something went wrong...")

conn.close()

