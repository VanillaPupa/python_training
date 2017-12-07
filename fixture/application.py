from selenium import webdriver
from fixture.group import GroupHelper
from fixture.user import UserHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)
        self.session = SessionHelper(self)
        self.wd.get("http://localhost/addressbook/")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()