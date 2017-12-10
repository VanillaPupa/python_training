from model.user import User


def test_add_user(app, json_users):
    contact = json_users
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