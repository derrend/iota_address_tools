#!/usr/bin/python3
import datetime
import random
import string
from sys import argv

from sub_seed_generator_v1 import seed_generate
from iota.crypto.addresses import AddressGenerator

def help_text():
    text = '''
    Keywords:
    help    Displays help text

    Arguments:
    (vanity_text, report_interval)
    '''
    print(text)


def vanity_seed_generator(vanity_text, report_interval=False):
    """Generates iota seed whose first subaddress begins with vanity_text

    Type:
        Function

    Args:
        vanity_text  (str object, required) string
        report_interval  (int object, optional) reports progress via standard output at designated intervals if defined

    Returns:
        None
    """

    if report_interval < 0:
        raise ValueError('Report interval cannot be negative')

    count = 0
    while True:
        secret = "".join([random.choice(string.ascii_letters + string.digits) for i in range(64)])
        seed = next(seed_generate(secret, 0, 1))

        ag = AddressGenerator(seed, checksum=True)
        address = str(ag.get_addresses(0)[0])

        if vanity_text in address[:len(vanity_text)]:
            print()
            print('Count:   ', count)
            print('Secret:  ', secret)
            print('Seed:    ', seed)
            print('Address: ', address)
            print()
            break

        if report_interval:
            if count % int(report_interval) == 0:
                print('Count:   ', str(count) + '\t', datetime.datetime.now() - datetime.timedelta(hours=-10))

        count += 1

# # Debug
# print(len(argv))
# for i in argv: print(i)

if __name__ == '__main__':
    if len(argv) is 1:
        help_text()
    elif len(argv) is 2 and argv[1].lower() == 'help':
        help_text()
    elif len(argv) is 2:
        vanity_seed_generator(argv[1].upper())
    elif len(argv) is 3:
        vanity_seed_generator(argv[1].upper(), int(argv[2]))
    else:
        raise TypeError('{} takes from 0 to 2 positional arguments but {} were given'.format(argv[0], len(argv) - 1))
