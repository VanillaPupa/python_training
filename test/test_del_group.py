from model.group import Group
import random


def test_del_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name4del"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        sorted_ui_groups = sorted(app.group.get_group_list(), key=Group.id_or_max)
        sorted_new_groups = sorted(new_groups, key=Group.id_or_max)
        indexes = range(len(new_groups))
        eq_flags = [sorted_ui_groups[n].name == sorted_new_groups[n].name and sorted_ui_groups[n].id == sorted_new_groups[n].id for n in indexes]
        result = all(eq_flags)
        assert result
