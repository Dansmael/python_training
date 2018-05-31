
from model.contact import Contact


def test_edit_link(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_link(Contact(first_name="first name1", last_name="last name1", address="address",
                               first_phone="+79991112233", second_phone="+79991112244", first_mail="mail@mail.ru",
                               second_mail="second mail2"))
    app.session.logout()


def test_edit_det(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_by_details(Contact(first_name="first name2", last_name="last name2", address="address",
                               first_phone="det phone", second_phone="det2 phone", first_mail="det1 mail",
                               second_mail="det2 mail"))
    app.session.logout()