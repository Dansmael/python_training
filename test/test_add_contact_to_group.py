from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="first_name1", last_name="last_name1", address="address1",
            home_phone="home 111", mobile_phone="mobile 3333", work_phone="work_852", secondary_phone="secondary1",
            email="email11", email2="email12", email3="email13"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_group = db.get_group_list()
    group = random.choice(old_group)

    app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = app.contact.get_contact_list_from_group_page(group.id)
    orm_contacts_in_group = orm.get_contacts_in_group(group)
    assert contacts_in_group == orm_contacts_in_group