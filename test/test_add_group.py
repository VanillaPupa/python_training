from model.group import Group


def test_create_group(app):
    old_groups = app.group.get_group_list()
    group_form = Group(name="Test group", header="Header 4 group", footer="Footer 4 group")
    app.group.create(group_form)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_create_empty_group(app):
    old_groups = app.group.get_group_list()
    group_form = Group(name="", header="", footer="")
    app.group.create(group_form)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)