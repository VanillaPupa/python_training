from model.group import Group


def test_create_group(app, db, json_groups):
    group_form = json_groups
    old_groups = db.get_group_list()
    app.group.create(group_form)
    new_groups = db.get_group_list()
    old_groups.append(group_form)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

