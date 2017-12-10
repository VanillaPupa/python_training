from model.user import User
import pytest
from data.users import constant as testdata


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