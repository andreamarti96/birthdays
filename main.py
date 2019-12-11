#! /usr/bin/env python3

import sys
from birthdays_package.birthdays import return_birthday

if len(sys.argv) == 3:
    user_input = sys.argv[1] + " " + sys.argv[2]
else:
    print("Enter: name username")
    exit()

return_birthday(user_input)
