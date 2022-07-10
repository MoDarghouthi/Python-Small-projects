import random
import string

AllChars = string.ascii_letters + string.digits + string.punctuation


def passGenerator(length):
    genPassword = "".join(random.sample(AllChars,length))
    return genPassword



PASSLENGTH = 20 #desired password length
password = passGenerator(PASSLENGTH)
print(password)