#!/usr/bin/python3
# Builtins
import string
import random
from sys import argv

# Modules
from modules.seed_generate import seed_generator
from modules.address_generate import address_generator


def help_text():
    text = '''
    Keywords:
    help    Displays help text
    random  Generates seed from random secret

    Arguments:
    (secret, seed_start=0, seed_stop=1, address_start=0, address_depth=1)
    '''
    print(text)


def reserved_text():
    text = '''
    'help' and 'random' cannot be used as secrets
    '''
    print(text)


# # Debug
# print(len(argv))
# for i in argv: print(i)

if __name__ == '__main__':
    # ()
    if len(argv) == 1:
        help_text()

    # (secret)
    if len(argv) == 2:
        # Display help text
        if argv[1].lower() == 'help':
            help_text()

        # Create random secret
        elif argv[1].lower() == 'random':
            secret = "".join([random.choice(string.ascii_letters + string.digits) for i in range(64)])
            print('Secret:', secret)

            seed = next(seed_generator(secret))
            print('Seed 0:', seed)

            address_generator(seed)

        # Generate seed from secret
        else:
            seed = next(seed_generator(argv[1]))
            print('Seed 0:', seed)

            address_generator(seed)

    # (secret, seed_start=0, seed_stop=1, address_start=0, address_depth=1)
    if len(argv) > 2:
        # Display reserved text
        if argv[1].lower() == 'help' or argv[1].lower() == 'random':
            reserved_text()

        # Seed target
        elif len(argv) == 3:
            seed = next(seed_generator(argv[1], int(argv[2]), int(argv[2]) + 1))
            print('Seed {}:'.format(argv[2]), seed)

        # Seed range
        elif len(argv) == 4:
            sg = seed_generator(argv[1], int(argv[2]), int(argv[3]))

            count = int(argv[2])
            for seed in sg:
                print('Seed {}:'.format(count), seed)
                count += 1

        # Address target
        elif len(argv) == 5:
            sg = seed_generator(argv[1], int(argv[2]), int(argv[3]))

            count = int(argv[2])
            for seed in sg:
                print('Seed {}:'.format(count), seed)

                address_generator(seed, int(argv[4]))
                count += 1

        # Address depth
        elif len(argv) == 6:
            sg = seed_generator(argv[1], int(argv[2]), int(argv[3]))

            count = int(argv[2])
            for seed in sg:
                print('Seed {}:'.format(count), seed)

                if not int(argv[5]) == 0:
                    address_generator(seed, int(argv[4]), int(argv[5]))

                count += 1

        # Too many arguments
        else:
            raise TypeError('{} takes from 0 to 5 positional arguments but {} were given'.format(argv[0], len(argv) - 1))
