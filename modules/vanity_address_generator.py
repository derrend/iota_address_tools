#!/usr/bin/python3
# Builtins
import datetime
import random
import string

# Modules
from modules.seed_generator import seed_generate

# Third party
from iota.crypto.addresses import AddressGenerator


def vanity_address_generate(vanity_text, report_interval=False):
    """Generates iota seed whose first subaddress begins with vanity_text

    Type:
        Function

    Args:
        vanity_text  (str object, required) string
        report_interval  (int object, optional) reports progress via standard output at designated intervals if defined

    Returns:
        None
    """

    # Tests
    if report_interval < 0:
        raise ValueError('Report interval cannot be negative')

    if type(vanity_text) is not str:
        raise TypeError('Vanity text must be type str')

    for char in vanity_text.upper():
        if char not in string.ascii_uppercase + '9':
            raise ValueError('Vanity text must only contain chars A-Z and 9')

    # Brute force loop
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

        # Report
        if report_interval:
            if count % int(report_interval) == 0:
                print('Count:   ', str(count) + '\t', datetime.datetime.now() - datetime.timedelta(hours=-10))

        count += 1
