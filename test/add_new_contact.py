# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(first_name="first name", last_name="last name", address="address",
                            first_phone="first phone", second_phone="second phone", first_mail="first mail",
                            second_mail="second mail"))
    app.logout()


