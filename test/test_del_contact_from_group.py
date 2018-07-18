from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="first name"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_group = db.get_group_list()
    group = random.choice(old_group)

    app.contact.add_contact_to_group(contact.id, group.id)