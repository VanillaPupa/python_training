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
        user_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, deprecated from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, deprecated) = row
                list.append(User(firstname=firstname, lastname=lastname, address=address, user_id=str(id), deprecated=deprecated))
            for n in range(len(list)):
                if list[n].deprecated is None:
                    user_list.append(list[n])
        finally:
            cursor.close()
        return user_list

    def destroy(self):
        self.connection.close()
