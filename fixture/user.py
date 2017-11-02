from model.user import User


class UserHelper:

    def __init__(self, app):
        self.app = app

    def create_user(self, app, contact, username, password):
        app.session.login(username, password)
        self.add_user(contact)
        app.session.logout()

    def delete_first_user(self, app, username, password):
        app.session.login(username, password)
        self.delete_first()
        app.session.logout()

    def update_first_user(self, app, contact, username, password):
        app.session.login(username, password)
        self.update_first(contact)
        # app.session.logout()

    def add_user(self, contact):
        wd = self.app.wd
        # init adding user
        wd.find_element_by_link_text("add new").click()
        # fill user form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.hometel)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobiletel)
        # submit user creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first(self):
        wd = self.app.wd
        # select first user
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()

    def update_first(self, contact):
        wd = self.app.wd
        # select first user
        wd.find_element_by_name("selected[]").click()
        # open update form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill user form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        # submit user creation
        wd.find_element_by_name("update").click()
        