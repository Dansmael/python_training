import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_not_in_group(Group(id='161'))
#    cursor.execute("select * from group_list")
    for item in l:
        print(item)
    print(len(l))
finally:
    pass