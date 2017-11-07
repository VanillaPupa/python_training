class UserHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        # init adding user
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(contact)
        # submit user creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first(self):
        wd = self.app.wd
        self.select_first_user()
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
        self.fill_user_form(contact)
        # submit user update
        wd.find_element_by_name("update").click()

    def select_first_user(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_user_form(self, contact):
        wd = self.app.wd
        if contact.firstname is not None:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.lastname is not None:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.address is not None:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.email is not None:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
        if contact.email2 is not None:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.hometel is not None:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.hometel)
        if contact.mobiletel is not None:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobiletel)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    # def create_user(self, app, contact, username, password):
        # app.session.login(username, password)
        # self.add_user(contact)
        # app.session.logout()

    # def delete_first_user(self, app, username, password):
        # app.session.login(username, password)
        # self.delete_first()
        # app.session.logout()

    # def update_first_user(self, app, contact, username, password):
        # app.session.login(username, password)
        # self.update_first(contact)
        # app.session.logout()
