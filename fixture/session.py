class SessionHelper:

    def __init__(self, app):
        self.app = app

# Login

    def ensure_login(self, username, password):
        wd = self.app.wd
        # Если уже залогинен, то проверка с каким username
        if self.is_logged_in():
            # Если залогинен с нужным username, то ок, иначе разлогиниться
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    # Проверка, что вход уже выполнен
    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    # Получение имени пользователя
    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

    # Заполнение полей формы логина
    def login(self, username, password):
        wd = self.app.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

# Logout

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    # Выход из системы, если залогинен
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

