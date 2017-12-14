from model.user import User


def test_add_user(app, db, data_users, check_ui):
    contact = data_users
    # формирование списка контактов
    old_user_list = db.get_user_list()
    # добавление контакта
    app.user.add(contact)
    # формирование нового списка пользователей
    new_user_list = db.get_user_list()
    # проверка, что новый список длиннее старого на 1
    assert len(old_user_list) + 1 == len(new_user_list)
    # добавление контакта в старый список
    old_user_list.append(contact)
    # проверка совпадения контактов из старого и нового списков
    # ПОТЕРЯЛСЯ ID у добавленного элемента
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)