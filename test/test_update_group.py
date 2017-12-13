from model.group import Group
import random


def test_update_some_group(app, db, check_ui, data_groups):
    updated_group_form = data_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name4update"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    updated_group_form.id = group.id
    app.group.update_by_id(group.id, updated_group_form)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    # Надо взять неизвестный элемент списка, у которого id = group.id
    # и перезаписать его с параметрами updated_group_form
    # old_groups[index].id == group.id
    # old_groups[index] = updated_group_form
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(db.get_group_list(), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
