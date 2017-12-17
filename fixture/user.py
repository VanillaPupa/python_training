from model.user import User
import re


class UserHelper:

    def __init__(self, app):
        self.app = app

    # Получение списка контактов

    user_list_cache = None

    def get_user_list(self):
        if self.user_list_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.user_list_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.user_list_cache.append(User(firstname=firstname, lastname=lastname, address=address, user_id=id,
                                                 all_phones_from_home_page=all_phones,
                                                 all_emails_from_home_page=all_emails))
        return list(self.user_list_cache)

    # Методы для создания контакта

    def add(self, contact):
        wd = self.app.wd
        # init adding user
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(contact)
        # submit user creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.user_list_cache = None

    # Методы для редактирования контакта

    def open_form_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        # Поиск элемента по индексу и нажатие на кнопку Edit
        link = "edit.php?id=" + str(id)
        wd.find_element_by_css_selector("a[href='%s']" % link).click()

    def open_form_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # Поиск элемента по индексу и нажатие на кнопку Edit
        wd.find_elements_by_css_selector("img[title='Edit']")[index].click()

    def update_by_id(self, id, contact):
        wd = self.app.wd
        self.open_form_to_edit_by_id(id)
        self.fill_user_form(contact)
        # submit user update
        wd.find_element_by_name("update").click()
        self.user_list_cache = None

    def update_by_index(self, index, contact):
        wd = self.app.wd
        self.open_form_to_edit_by_index(index)
        self.fill_user_form(contact)
        # submit user update
        wd.find_element_by_name("update").click()
        self.user_list_cache = None

    def update_first(self, contact):
        self.update_by_index(0, contact)

    # Методы для удаления контакта

    def delete_by_id(self, id):
        wd = self.app.wd
        self.select_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.user_list_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        self.select_user_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.user_list_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    # Просмотр контакта

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector("img[title='Details']")[index].click()

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_form_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        additionalphone = wd.find_element_by_name("phone2").get_attribute("value")
        return User(firstname=firstname, lastname=lastname, address=address, user_id=id,
                    email=email1, email2=email2, email3=email3,
                    homephone=homephone, workphone=workphone, mobilephone=mobilephone, additionalphone=additionalphone)

    def get_user_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        additionalphone = re.search("P: (.*)", text).group(1)
        return User(homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                    additionalphone=additionalphone)

    # Методы для выбора контакта

    def select_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    # Заполнение формы

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
        if contact.email3 is not None:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.homephone is not None:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.homephone)
        if contact.mobilephone is not None:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        if contact.workphone is not None:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.workphone)
        if contact.additionalphone is not None:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.additionalphone)

    # Другие методы

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
