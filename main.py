import argparse
from birthdays_package.birthdays_module import (return_data,
return_index, return_set)

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

    args = parser.parse_args()
    i = return_index(args.name)
    dataset = return_data()
    if i is None:
        print("error")
    else:
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

