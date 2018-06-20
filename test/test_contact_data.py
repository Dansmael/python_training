
from model.contact import Contact
from random import randrange
import re

def test_data_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first name", last_name="last name", address="address",
                                   home_phone="first phone", mobile_phone="second phone", email="first@mail.ru mail",
                                   email2="second mail", email3="mail@mail.com"))
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_mails_from_homepage == merge_mails_like_on_homepage(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]","",s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.work_phone,
                                        contact.mobile_phone, contact.secondary_phone]))))


def merge_mails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))



