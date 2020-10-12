import random
from address_values import *
from names import *


def get_random_address():
    number = random.randint(1, 999) if random.randint(0, 5) else random.randint(1, 5000)
    street = street_names[random.randint(0, len(street_names)-1)]
    extension = valid_streets[random.randint(0, len(valid_streets)-1)]
    rand_zip = zips[random.randint(0, len(zips)-1)]
    town = rand_zip[0]
    state = rand_zip[1]
    zip = rand_zip[2]
    return '{} {} {}, {}, {} {}'.format(number, street, extension, town, state, zip)


def get_random_name():
    first_name = first_names[random.randint(0, len(first_names)-1)]
    last_name = last_names[random.randint(0, len(last_names)-1)]
    return '{} {}'.format(first_name, last_name)


def get_random_phone(num=""):
    if len(num) < 10:
        return get_random_phone(num + str(random.randint(0, 9)))
    return num


if __name__ == '__main__':
    print(get_random_name())
    print(get_random_address())
    print(get_random_phone())
