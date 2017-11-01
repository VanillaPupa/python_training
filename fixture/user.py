from fixture.session import SessionHelper
from model.user import User


class UserHelper:

    def __init__(self, app):
        self.app = app
        self.session = SessionHelper(app)

    def create_user(self, username, password, firstname, lastname, address, email, email2, hometel, mobiletel):
        self.session.login(username, password)
        self.add_user(User(firstname, lastname, address, email, email2, hometel, mobiletel))
        self.session.logout()

    def add_user(self, user):
        wd = self.app.wd
        # init adding user
        wd.find_element_by_link_text("add new").click()
        # fill group form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(user.email2)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.hometel)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(user.mobiletel)
        # submit user creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()