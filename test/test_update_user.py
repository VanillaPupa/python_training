from model.user import User
from random import randrange


def test_update_some_user(app):
    if app.user.count() == 0:
        new_contact = User(firstname="Sherlock", lastname="Holmes",
                   address="221b, Baker Street, London, UK", email="Sherlock@museum.com",
                   email2="Holmes@museum.com", email3="HolmesWatson@museum.com",homephone="321-32-13",
                   mobilephone="+441712223355", workphone="123 12 31", additionalphone="+(44)1715553322")
        app.user.add(new_contact)
        app.user.open_home_page()
    # формирование старого списка
    old_user_list = app.user.get_user_list()
    # выбор индекса
    index = randrange(len(old_user_list))
    # новый объект
    contact = User(firstname="John H.", lastname="Watson", email="JohnH.Watson@Museum.com", email2="Dr.Watson@Museum.com")
    # запись id в новый объект
    contact.id = old_user_list[index].id
    # перезапись строчки
    app.user.update_by_index(index, contact)
    # формирование нового списка
    new_user_list = app.user.get_user_list()
    # сравнение длин списков
    assert len(old_user_list) == len(new_user_list)
    # перезапись строчки старого списка
    old_user_list[index] = contact
    # сравнение отсортированных списков
    assert sorted(old_user_list, key=lambda user: user.id) == sorted(new_user_list, key=lambda user: user.id)

