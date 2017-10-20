# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import User
from login_logout import *


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class Second_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_user(self):
        wd = self.wd
        open_home_page(wd)
        login(wd)
        self.add_user(wd, User(firstname="Sherlock", lastname="Holmes", address="221b, Baker Street, London, UK",
                 email="Sherlock@Museum.com", email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355"))
        logout(wd)

    def add_user(self, wd, user):
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

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
