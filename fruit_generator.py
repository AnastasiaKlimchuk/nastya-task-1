import random
import string

MAX_TITLE_LENGTH = 10
MAX_ID_LENGTH = 10
MAX_FRUITS_LENGTH = 15

SIZES = ['small', 'medium', 'large']


# size of random string is always begin from 3
def get_random_string(size):
    return ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=random.randint(3, size)))


def get_random_size():
    return SIZES[random.randint(0, len(SIZES) - 1)]


def create(id, size):
    title = get_random_string(MAX_TITLE_LENGTH)

    if size is None:
        size = get_random_size()

    return {
        'id': id,
        'title': title,
        'size': size
    }


def create_list(size):
    fruits = list()

    for _ in range(random.randint(1, MAX_FRUITS_LENGTH)):
        id = get_random_string(MAX_ID_LENGTH)
        fruit = create(id, size)

        fruits.append(fruit)

    return fruits
