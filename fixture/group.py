from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    # Получение списка групп

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, group_id=id))
        return list(self.group_cache)

    # Методы для создания группы

    def create(self, group_form):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group_form)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    # Методы для редактирования группы

    def update_by_index(self, index, group_form):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_index(index)
        # open update form
        wd.find_element_by_xpath("//div[@id='content']/form/input[6]").click()
        self.fill_group_form(group_form)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def update_by_id(self, id, group_form):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_id(id)
        # open update form
        wd.find_element_by_xpath("//div[@id='content']/form/input[6]").click()
        self.fill_group_form(group_form)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def update_first(self, group_form):
        self.update_by_index(0, group_form)

    # Методы для удаления группы

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    # Методы для выбора группы

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    # Заполнение формы

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

    # Просмотр списка групп

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    # Другие методы

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
