# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="first name", last_name="last name", address="address",
                               first_phone="first phone", second_phone="second phone", first_mail="first mail",
                               second_mail="second mail"))
    app.session.logout()
