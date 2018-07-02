from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))


def random_phone(prefix, maxlen):
    symbol = string.digits + "-"*4 + "(" + ")"
    return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))


def random_email(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + "@" + "."*3 + "-" + "_"
    return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))


testdata= [Contact(first_name=random_string("first name", 10), last_name=random_string("last name", 10),
                  address=random_string("address", 20),
                  home_phone=random_phone("home_phone", 17), mobile_phone=random_phone("mobile_phone", 17),
                  work_phone=random_phone("work_phone", 17), secondary_phone=random_phone("secondary_phone", 17),
                  email=random_email("email", 20), email2=random_email("email2", 20), email3=random_email("email3", 20))
           for i in range(4)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
