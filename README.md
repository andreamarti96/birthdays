**FIND PEOPLE BIRTHDAYS**

In our repository, you find *main.py* which returns the birthdays (and other info) of several well-known people given a valid input. 
To be able to run the code, you need to insert your credentials (username and password).
Steps:

**How to:**

Insert the name/s of the person you want to know the birthday of and your right credentials. 
This is the outcome you will may receive if you type this options:
```
$ python3 main.py 'Donald Trump' -u -c username -p password
  Username Correct
  Password Correct
  You are allowed to access the program!
  People born in the same century of DONALD TRUMP:
  Donald Trump: 06/14/1946
  Rowan Atkinson: 01/06/1955
```
In the case of incorrect credentials, the program will return that either the password or the username is invalid.

**How to populate the database:**

If you want to only access the database, because you are already registered, you can run the *main.py* only. 
Instead, if you are registering for the first time you have to use the dbmanager.py in which you can find some useful instructions.

**Add a new user:**

To add a new user into the database, these are the arguments you need to insert in *dbmanager.py* file:
```
-h, --help: tells you the possible arguments you can insert
-a: username
-p: password
$ python dbmanager.py -a username -p password
  Username username successfully added
```
**Check the validity:**

To check if your credentials are valid, please insert in *dbmanager.py*:
```
-h, --help: tells you the possible arguments you can insert
-c: username
-p: password
$ python dbmanager.py -c username -p password
```
**Let’s now use the application!**

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
If you insert a name that is not found in the database, the program returns the following statement:
```
$ python main.py 'Alan Turing' -c username -p password
  error
```
**Verbosity:**

You can view your output in three different ways:
```
-v: shows the name, the birthday and the day of death.
-vv or more: returns what returns -v plus the hometown.
-u: shows the name of the person/s (and their birthdays) born in the same century.
```
Note: If you don't put any -v, you will get only the name and the date of the birthday.

**PEP-8 and PEP-257**:

All the python modules used the standard rules of PEP-8 and PEP-257 for codes and dostrings to make the code documentable and consistent.

**Test**:

We can test our code using three functions in order to check our program. The tests can be found in the folder named *tests/test_csv/*, 
we use this module to test the correct creation of csv file. 
You can repeat the tests running the code: *python3 -m unittest -v -b tests/test_csv.py.* The output you receive is the following:
```
$ python3 -m unittest -v -b tests/test_csv.py
  test_empty_datafile (tests.test_csv.TestMain)
  Check the presence of data inside the csv file. ... ok
  test_no_datafile (tests.test_csv.TestMain)
  Check if there is a csv file. ... ok
  test_valid_extension (tests.test_csv.TestMain)
  Check the extension of the file. ... ok

----------------------------------------------------------------------
  Ran 3 tests in 0.001s

  OK 
 ```
**Authors:**

We are the **32Bit** group:

*Donè Edoardo*,
*Martignago Andrea*,
*Menazza Francesco*,
*Venturini Isaac*.

**License:**
GNU GENERAL PUBLIC LICENSE

## Credits:

Code is taken from the nice [practice Python](https://www.practicepython.org/) website from Michele Pratusevich and is released with a [CC-BY](https://www.practicepython.org/about/) license.
