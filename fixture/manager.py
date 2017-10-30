from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.user import UserHelper
from model.user import User
from model.group import Group


class HelperManager:

    def __init__(self, app):
        self.app = app
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def create_group(self, username, password, name, header, footer):
        self.session.login(username, password)
        self.group.open_groups_page()
        self.group.create(Group(name, header, footer))
        self.session.logout()

    def create_user(self, username, password, firstname, lastname, address, email, email2, hometel, mobiletel):
        wd = self.app.wd
        self.session.login(username, password)
        self.user.add(User(firstname, lastname, address, email, email2, hometel, mobiletel))
        self.session.logout()
