import pymysql
from model.group import Group
from model.user import User


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(group_id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_user_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, deprecated from addressbook")
            for (id, firstname, lastname, address, deprecated) in cursor:
                list.append(User(firstname=firstname, lastname=lastname, address=address, user_id=str(id),
                                 deprecated=deprecated))
            user_list = [user for user in list if user.deprecated is None]
        finally:
            cursor.close()
        return user_list

    def destroy(self):
        self.connection.close()
