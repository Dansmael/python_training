
from model.group import Group
import random

def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
#    index = randrange(len(old_groups))
    group_data = Group(name="New group-changed", header="header-changed", footer="footer-changed")
#    group.id = old_groups[index].id
    app.group.edit_group_by_id(group.id, group_data)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    group_data.id = group.id
    old_groups.remove(group)
    old_groups.append(group_data)
    s_old_g = sorted(old_groups, key=Group.id_or_max)
    s_new_g = sorted(new_groups, key=Group.id_or_max)
    assert s_old_g == s_new_g

    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list = map(clean, db.get_group_list())

        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="New group"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="New group - MFG"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

