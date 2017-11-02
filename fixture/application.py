from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper
from fixture.user import UserHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)
        self.session = SessionHelper(self)
        self.wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()