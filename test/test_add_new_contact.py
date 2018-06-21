# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

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
                  work_phone=random_phone("work_phone", 17), secondary_phone=random_phone("secondary_phone", 17))
#                  email=random_email("email", 20), email2=random_email("email2", 20), email3=random_email("email3", 20))
           for i in range(4)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
