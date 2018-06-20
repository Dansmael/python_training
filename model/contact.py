
from sys import maxsize

class Contact:

    def __init__(self, first_name=None, last_name=None, id=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, secondary_phone=None,
                 email=None, email2=None, email3=None, all_phones_from_homepage=None, all_mails_from_homepage=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_mails_from_homepage = all_mails_from_homepage


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.first_name)

    def __eq__(self, other):
        return self.id == None or other.id == None or self.id == other.id \
               and self.last_name == other.last_name \
               and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize