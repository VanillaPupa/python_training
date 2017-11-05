class GroupHelper:

    def __init__(self, app):
        self.app = app

    # def create_group(self, app, group_form, username, password):
        # app.session.login(username, password)
        # self.create(group_form)
        # app.session.logout()

    # def delete_first_group(self, app, username, password):
        # app.session.login(username, password)
        # self.delete_first()
        # app.session.logout()

    # def update_first_group(self, app, group_form, username, password):
        # app.session.login(username, password)
        # self.update_first(group_form)
        # app.session.logout()

    def create(self, group_form):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group_form)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def update_first(self, group_form):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open update form
        wd.find_element_by_xpath("//div[@id='content']/form/input[6]").click()
        self.fill_group_form(group_form)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, group_form):
        wd = self.app.wd
        if group_form.name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group_form.name)
        if group_form.header is not None:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group_form.header)
        if group_form.footer is not None:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group_form.footer)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
