#!/usr/bin/python3
# Third party
from iota.crypto.addresses import AddressGenerator


def address_generator(seed, address_start=0, address_depth=1):
    """Generates iota addresses from a given seed to a desired depth

    Type:
        Function

    Args:
        secret  (str object, required) 81 character iota seed
        seed_start  (int object, required) integer defining subaddress starting point
        seed_start  (int object, required) integer defining subaddress ending point

    Returns:
        None
    """

    count = address_start
    ag = AddressGenerator(seed, checksum=True)

    for address in ag.get_addresses(address_start, address_depth):
        print('Address {}:'.format(count), address)
        count += 1
