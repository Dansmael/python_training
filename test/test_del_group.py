
from model.group import Group


def test_delete_firts_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.delete_first_group()
