import string
import random

nombre = "Alberto Moreno"
email = "alberto.moreno-fernandez.external@sogeti.com"
password = "Testing1234"

bad_email = "bad_email@noexiste,com"

def generate_invalid_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    invalid_email = random_string + "@gmail.com"
    return invalid_email

def generate_invalid_password():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    invalid_password = random_string
    return invalid_password