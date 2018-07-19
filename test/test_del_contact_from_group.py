from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="first_name1", last_name="last_name1", address="address1",
            home_phone="home 111", mobile_phone="mobile 3333", work_phone="work_852", secondary_phone="secondary1",
            email="email11", email2="email12", email3="email13"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    group_list = db.get_group_list()
    contact_list = db.get_contact_list()
    group_with_contacts = []
    for g in group_list:
        if len(orm.get_contacts_in_group(g)) != 0:
            group_with_contacts.append(g)
        return list(group_with_contacts)

    if len(group_with_contacts) == 0:
        contact = random.choice(contact_list)
        group = random.choice(group_list)
        app.contact.add_contact_to_group(contact.id, group.id)

    test_group = random.choice(group_with_contacts)
    test_contact = random.choice(orm.get_contacts_in_group(test_group))
    app.contact.del_contact_from_group(test_contact.id, test_group.id)

    contacts_in_group = app.contact.get_contact_list_from_group_page(test_group.id)
    orm_contacts_in_group = orm.get_contacts_in_group(test_group)
    assert contacts_in_group == orm_contacts_in_group