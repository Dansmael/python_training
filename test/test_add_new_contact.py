# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="first name", last_name="last name", address="address",
                      home_phone="first phone", mobile_phone="second phone", email="first@mail.ru mail",
                               email2="second mail", email3="mail@mail.com")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
