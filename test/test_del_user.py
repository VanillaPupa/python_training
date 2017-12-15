from model.user import User
import random


def test_del_some_user(app, db, check_ui):
    if app.user.count() == 0:
        contact = User(firstname="Sherlock", lastname="Holmes",
                   address="221b, Baker Street, London, UK", email="Sherlock@museum.com",
                   email2="Holmes@museum.com", email3="HolmesWatson@museum.com",homephone="321-32-13",
                   mobilephone="+441712223355", workphone="123 12 31", additionalphone="+(44)1715553322")
        app.user.add(contact)
        app.open_home_page()
    old_user_list = db.get_user_list()
    user = random.choice(old_user_list)
    app.user.delete_by_id(user.id)
    app.open_home_page()
    new_user_list = db.get_user_list()
    assert len(old_user_list) - 1 == len(new_user_list)
    old_user_list.remove(user)
    assert old_user_list == new_user_list
    if check_ui:
        assert sorted(new_user_list, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)
