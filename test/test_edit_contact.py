
from model.contact import Contact


def test_edit_link(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first name0"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="first name1", last_name="last name1", address="address",
                               first_phone="+79991112233", second_phone="+79991112244", first_mail="mail@mail.ru",
                               second_mail="second mail2")
    contact.id = old_contacts[0].id
    app.contact.edit_link(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_edit_det(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="first name1"))
#    app.contact.edit_by_details(Contact(first_name="first name2", last_name="last name2", address="address"))
