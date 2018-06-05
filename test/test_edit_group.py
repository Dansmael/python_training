
from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.edit(Group(name="New group - changed", header="header - changed", footer="footer - changed"))

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.modify_first_group(Group(name="New group - MFG"))

