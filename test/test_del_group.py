from model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        group_form = Group(name="Test group")
        app.group.create(group_form)
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
