from model.contact import Contact
import jsonpickle
import getopt
import sys
import os
import random
import string

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December")


def get_random_name():
    return "%s%s" % (get_random_string_uppercase(1), get_random_string_lowercase(3, 6))


def get_random_email():
    return "%s@%s.%s" % (
    get_random_string_lowercase(3, 6), get_random_string_lowercase(3, 6), get_random_string_lowercase(2, 4))


def get_random_address():
    return "%s%s" % (get_random_string_uppercase(1), get_random_string_lowercase(3, 6))


def get_random_text(max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def get_random_string_lowercase(min_len, max_len):
    return "".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(min_len, max_len))])


def get_random_string_uppercase(len):
    return "".join([random.choice(string.ascii_uppercase) for i in range(len)])


def get_random_string_digits(min_len, max_len):
    return "".join([random.choice(string.digits) for i in range(random.randrange(min_len, max_len))])


def get_random_day():
    return "".join(map(str, [random.randint(1, 31)]))


def get_random_year():
    return "".join(map(str, [random.randint(1980, 2000)]))


def get_random_months():
    return "".join([random.choice(months)])


test_data = [Contact(
    firstname=get_random_name(),
    middlename=get_random_name(),
    lastname=get_random_name(),
    nickname=get_random_name(),
    title=get_random_name(),
    company=get_random_name(),
    address=get_random_address(),
    homephone=get_random_string_digits(10, 11),
    mobilephone=get_random_string_digits(10, 11),
    workphone=get_random_string_digits(10, 11),
    fax=get_random_string_digits(10, 11),
    email=get_random_email(),
    email2=get_random_email(),
    email3=get_random_email(),
    homepage=get_random_email(),
    birthday_date=get_random_day(),
    birthday_month=get_random_months(),
    byear=get_random_year(),
    anniversary_date=get_random_day(),
    anniversary_month=get_random_months(),
    ayear=get_random_year(),
    address2=get_random_address(),
    secondaryphone=get_random_string_digits(10, 11),
    notes=get_random_text(10)) for i in range(n)] + [
              Contact(firstname="", lastname="", address="", homephone="", workphone="",
                      mobilephone="", secondaryphone="",
                      email="", email2="", email3="")]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)
with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
