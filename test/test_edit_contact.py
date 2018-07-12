
from model.contact import Contact
import random

def test_edit_link(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="first name0"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_data = Contact(first_name="first name1", last_name="last name1", address="address",
                      home_phone="+79991112233", mobile_phone="+79991112244", email="mail@mail.ru",
                               email2="second mail2")
    app.contact.edit_link_by_id(contact.id, contact_data)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    contact_data.id = contact.id
    old_contacts.remove(contact)
    old_contacts.append(contact_data)
    s_old_c = sorted(old_contacts, key=Contact.id_or_max)
    s_new_c = sorted(new_contacts, key=Contact.id_or_max)
    assert s_old_c == s_new_c
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_edit_det(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="first name1"))
#    app.contact.edit_by_details(Contact(first_name="first name2", last_name="last name2", address="address"))
