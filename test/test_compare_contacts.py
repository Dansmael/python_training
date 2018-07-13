from model.contact import Contact
import re

def test_compare_contacts(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="first name1", last_name="last name1", address="address",
                      home_phone="+79991112233", mobile_phone="+79991112244", email="mail@mail.ru",
                               email2="second mail2"))
#    db_c_list = db.get_contact_list()
#    app_c_list = app.contact.get_contact_list()
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    app_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    num_contacts = len(app_contacts)
    for index in range(0, num_contacts):
        assert app_contacts[index].first_name == db_contacts[index].first_name
        assert app_contacts[index].last_name == db_contacts[index].last_name
        assert app_contacts[index].address == db_contacts[index].address
        assert app_contacts[index].all_phones_from_homepage == all_phones_db(db_contacts[index])
        assert app_contacts[index].all_mails_from_homepage == all_mails_db(db_contacts[index])


def clear(s):
    return re.sub("[() -]", "", s)


def all_phones_db(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone,
                                        contact.work_phone, contact.secondary_phone]))))


def all_mails_db(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

