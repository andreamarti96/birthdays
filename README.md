# Find people Birthday's 

In our repository, you find *main.py* which returns the birthdays (and other info) of several well-known people given a valid input. 
To be able to run the code, you need to insert your credentials (username and password).

> **Note**: See below how dbmanager.py works in order to create a new user. 


# Usage

Insert the name/s of the person you want to know the birthday of and your right credentials. 
This is the outcome you will may receive if you type this options:
```
$ python3 main.py 'Donald Trump' -c test -p test
INFO:main_logger:Username Correct! Password Correct!
INFO:main_logger:You are allowed to access the program!

INFO:main_logger:DONALD TRUMP's birthday is: 06/14/1946

```
> **Note**: In case of incorrect credentials, the program will return that either the password or the username is invalid.

If you insert a name that is not found in the database, the program returns the following statement:
```
$ python main.py 'Alan Turing' -c username -p password
ERROR:main_logger:error
Person not found!
```
 

# How to populate the database:

If you want to only access the database, because you are already registered, you can run the *main.py* only. 
Instead, if you are registering for the first time you have to use the **dbmanager.py** in which you can find some useful instructions.

## Add a new user:

To add a new user into the database, these are the arguments you need to insert in *dbmanager.py* file:
```
-h, --help: tells you the possible arguments you can insert
-a: username
-p: password
$ python dbmanager.py -a username -p password
  Username username successfully added
```

> **Note**: for **testing** purposes, you can use **username: test** and **password: test**

## Check validity of credentials:

To check if your credentials are valid, please insert in *dbmanager.py*:
```
-h, --help: tells you the possible arguments you can insert
-c: username
-p: password
$ python dbmanager.py -c username -p password
```
## Available data

Once you have completed the registration or access process, you find out the birthdays and other info of people present in the 
*birthdays.csv* file, contained in *birthdays_package*. The database contains this information:
```
Name,              Birthday,    Death,        City
Donald Trump,      06/14/1946,  still alive,  New York
Ada Lovelace,      12/10/1815,  27/11/1852,   London
Benjamin Franklin, 01/17/1706,  17/04/1790,   Boston
Rowan Atkinson,    01/06/1955,  still alive,  Consett
Albert Einstein,   03/14/1879,  18/04/1955,   Ulm
```
> **Note:** Feel free to add new people as long as you respect the order of the columns. 

# Verbosity:

We used **logging** and **verboselogs** to handle different levels of verbosity. Please feel free to check either:

- *no verbosity:* basic information (name and birthday
- *verbosity 1 (-v):* more information about the person (name, birthday, death)
- *verbosity 2 (-vv):* name, birthday, death and city

> **Note**: the higher the level of verbosity the higher the quantity of messagges given by the program.


## PEP-8 and PEP-257:

All the python modules used the standard rules of PEP-8 and PEP-257 for codes and dostrings to make the code documentable and consistent.
All the documentation has been generated using **Spinx**.  
All the modules have passed the **pycodestyle** tests.

# Tests:

We built 4 tests in order to check our main functions. The tests can be found in the folder named *tests/test_main.py*.    
You can repeat the tests running the code: *python3 -m unittest -v -b tests/test_main.py.* The output you receive is the following:
```
$ python3 -m unittest -v -b tests/test_main.py 
test_empty_file (tests.test_main.TestMain)
Check the presence of data inside the csv file. ... ok
test_index (tests.test_main.TestMain)
Check if the index is False if person not found. ... ok
test_no_datafile (tests.test_main.TestMain)
Check if there is a csv file. ... ok
test_set (tests.test_main.TestMain)
Check if the set returns a meaningful value for an existent item. ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
 ```
# Authors:

We are the **32Bit** group:

- *Donè Edoardo* 
- *Martignago Andrea*
- *Menazza Francesco*
- *Venturin Isac*

**License:**
GNU GENERAL PUBLIC LICENSE

## Credits:

Code is taken from the nice [practice Python](https://www.practicepython.org/) website from Michele Pratusevich and is released with a [CC-BY](https://www.practicepython.org/about/) license.