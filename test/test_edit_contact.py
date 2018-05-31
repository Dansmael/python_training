
from model.contact import Contact


def test_edit_link(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_link(Contact(first_name="first name1", last_name="last name1", address="address",
                               first_phone="first phone", second_phone="second phone", first_mail="first mail",
                               second_mail="second mail2"))
    app.session.logout()


def test_edit_det(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_det(Contact(first_name="first name2", last_name="last name2", address="address",
                               first_phone="first phone", second_phone="second phone", first_mail="first mail",
                               second_mail="second mail"))
    app.session.logout()