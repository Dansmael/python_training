
from model.group import Group

def test_edit_group(app):
    app.group.edit(Group(name="New group - changed", header="header - changed", footer="footer - changed"))

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group - MFG"))
