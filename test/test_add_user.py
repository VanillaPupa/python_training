from model.user import User


def test_add_user(app):
    # формирование старого списка пользователей
    old_user_list = app.user.get_user_list()
    # данные для нового контакта
    contact = User(firstname="Sherlock", lastname="Holmes",
                   address="221b, Baker Street, London, UK", email="Sherlock@Museum.com",
                   email2="Holmes@Museum.com", homephone="3213213", mobilephone="+441712223355")
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