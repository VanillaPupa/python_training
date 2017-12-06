from model.user import User
import pytest
import random
import string


def random_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + ": " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits + "(" + ")" + "-" + "+" + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [User(firstname="", lastname="", address="", email="", email2="", email3="", homephone="", mobilephone="",
                 workphone="", additionalphone="")] + \
           [User(firstname=random_str("firstname", 10), lastname=random_str("lastname", 20),
                 address=random_str("address", 70), email=random_str("email", 20), email2=random_str("email2", 20),
                 email3=random_str("email3", 20), homephone=random_phone(10), mobilephone=random_phone(10),
                 workphone=random_phone(10), additionalphone=random_phone(10))for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, contact):
    old_user_list = app.user.get_user_list()
    # добавление контакта
    app.user.add(contact)
    # формирование нового списка пользователей
    new_user_list = app.user.get_user_list()
    # проверка, что новый список длиннее старого на 1
    assert len(old_user_list) + 1 == len(new_user_list)
    # добавление контакта в старый список
    old_user_list.append(contact)
    # проверка совпадения контактов из старого и нового списков
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)