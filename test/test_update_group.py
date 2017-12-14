from model.group import Group
import random


def test_update_some_group(app, db, check_ui, data_groups):
    updated_group_form = data_groups
    # Создание тестовой группы, если список пуст
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name4update"))
    # Получение текущего списка групп из БД
    old_groups = db.get_group_list()
    # Рандомный выбор элемента списка
    random_group = random.choice(old_groups)
    # Запись id выбранной группы в тестовые данные
    updated_group_form.id = random_group.id
    # Модификация группы
    app.group.update_by_id(random_group.id, updated_group_form)
    # Получение нового списка групп из БД
    new_groups = db.get_group_list()
    # Проверка, что длины старого и нового списка совпадают
    assert len(old_groups) == len(new_groups)
    # Создание обновлённого старого списка, который содержит обновлёную группу
    updated_old_groups = [group if group.id != updated_group_form.id else updated_group_form for group in old_groups]
    # Проверка, что обновленный старый список равен новому списку
    assert sorted(updated_old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        # Проверка, что новый список из UI совпадает с списком из БД
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
