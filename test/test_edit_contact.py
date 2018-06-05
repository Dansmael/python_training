
from model.contact import Contact


def test_edit_link(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first name0"))
    app.contact.edit_link(Contact(first_name="first name1", last_name="last name1", address="address",
                               first_phone="+79991112233", second_phone="+79991112244", first_mail="mail@mail.ru",
                               second_mail="second mail2"))


def test_edit_det(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first name1"))
    app.contact.edit_by_details(Contact(first_name="first name2", last_name="last name2", address="address"))
