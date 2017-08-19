""" Write a function which checks whether an IP address is valid.

    >>> is_valid_ip("128.15.0.6")
    True

    >>> is_valid_ip("")
    False

    >>> is_valid_ip("another string")
    False

    >>> is_valid_ip("this.thing.here.10")
    False

    >>> is_valid_ip("0.0.0.0")
    True

    >>> is_valid_ip("....")
    False

"""


def is_valid_ip(ip_address):

    substrings = ip_address.split(".")

    if len(substrings) != 4:
        return False

    for num in substrings:
        if 1 > len(num) > 3:
            return False
        for char in num:
            if char.isdigit() is False:
                return False

        if int(num) > 255:
            return False

    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO GO GO!\n"
