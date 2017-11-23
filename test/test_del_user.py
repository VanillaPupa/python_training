from model.user import User
from random import randrange


def test_del_some_user(app):
    if app.user.count() == 0:
        contact = User(firstname="Sherlock", lastname="Holmes",
                       address="221b, Baker Street, London, UK", email="Sherlock@Museum.com",
                       email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355")
        app.user.add(contact)
        app.user.open_home_page()
    old_user_list = app.user.get_user_list()
    index = randrange(len(old_user_list))
    app.user.delete_by_index(index)
    app.user.open_home_page()
    new_user_list = app.user.get_user_list()
    assert len(old_user_list) - 1 == len(new_user_list)
    old_user_list[index:index+1] = []
    assert old_user_list == new_user_list
