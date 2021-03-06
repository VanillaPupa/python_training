from sys import maxsize


class User:

    def __init__(self, firstname=None, lastname=None, address=None, email=None, email2=None, email3=None, user_id=None,
                 homephone=None, workphone=None, mobilephone=None, additionalphone=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None, deprecated=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.id = user_id
        self.workphone = workphone
        self.additionalphone = additionalphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.deprecated = deprecated

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.deprecated)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
