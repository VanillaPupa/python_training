from model.user import User
from random import randrange


def test_update_some_user(app):
    if app.user.count() == 0:
        contact = User(firstname="Sherlock", lastname="Holmes",
                       address="221b, Baker Street, London, UK", email="Sherlock@Museum.com",
                       email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355")
        app.user.add(contact)
        app.user.open_home_page()
    old_user_list = app.user.get_user_list()
    index = randrange(len(old_user_list))
    contact = User(firstname="John H.", lastname="Watson", email="JohnH.Watson@Museum.com", email2="Dr.Watson@Museum.com")
    contact.id = old_user_list[index].id
    app.user.update_by_index(index, contact)
    new_user_list = app.user.get_user_list()
    assert len(old_user_list) == len(new_user_list)
    old_user_list[index] = contact
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)