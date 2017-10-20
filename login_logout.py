def open_home_page(wd):
    wd.get("http://localhost/addressbook/")


def login(wd):
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys("admin")
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys("secret")
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


def logout(wd):
    wd.find_element_by_link_text("Logout").click()