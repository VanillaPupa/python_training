from model.user import User
from random import randrange


def test_del_some_user(app):
    if app.user.count() == 0:
        contact = User(firstname="Sherlock", lastname="Holmes",
                   address="221b, Baker Street, London, UK", email="Sherlock@museum.com",
                   email2="Holmes@museum.com", email3="HolmesWatson@museum.com",homephone="321-32-13",
                   mobilephone="+441712223355", workphone="123 12 31", additionalphone="+(44)1715553322")
        app.user.add(contact)
        app.open_home_page()
    old_user_list = app.user.get_user_list()
    index = randrange(len(old_user_list))
    app.user.delete_by_index(index)
    app.open_home_page()
    new_user_list = app.user.get_user_list()
    assert len(old_user_list) - 1 == len(new_user_list)
    old_user_list[index:index+1] = []
    assert old_user_list == new_user_list
