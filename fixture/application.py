from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.manager import HelperManager


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.manager = HelperManager(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()