#!/usr/bin/python3
# Builtins
from sys import argv

# Modules
from modules.vanity_address_generate import vanity_address_generator


def help_text():
    text = '''
    Keywords:
    help    Displays help text

    Arguments:
    (vanity_text, report_interval)
    '''
    print(text)


def main(argv):
    if len(argv) is 1:
        help_text()
    elif len(argv) is 2 and argv[1].lower() == 'help':
        help_text()
    elif len(argv) is 2:
        vanity_address_generator(argv[1].upper())
    elif len(argv) is 3:
        vanity_address_generator(argv[1].upper(), int(argv[2]))
    else:
        raise TypeError('{} takes from 0 to 2 positional arguments but {} were given'.format(argv[0], len(argv) - 1))


# # Debug
# print(len(argv))
# for i in argv: print(i)

if __name__ == '__main__':
    main(argv)
