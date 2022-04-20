import string
import random


# characters to generate password from
characters = list(string.ascii_letters + string.digits + "@#$%")


def generate_random_password(length=10):

    # shuffling the characters
    random.shuffle(characters)

    # picking random characters from the list
    password = []
    for _ in range(length):
        password.append(random.choice(characters))

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to string
    # printing the list
    return "".join(password)
