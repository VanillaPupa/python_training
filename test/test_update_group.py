from model.group import Group
from random import randrange


def test_update_some_group(app):
    if app.group.count() == 0:
        group_form = Group(name="Test group")
        app.group.create(group_form)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group_form = Group(name="Updated group", header="Updated Header 4 group", footer="Updated Footer 4 group")
    group_form.id = old_groups[index].id
    app.group.update_by_index(index, group_form)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group_form
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_update_name_first_group(app):
    # if app.group.count() == 0:
        # group_form = Group(name="Test group")
        # app.group.create(group_form)
    # old_groups = app.group.get_group_list()
    # group_form = Group(name="Updated Name")
    # app.group.update_first(group_form)
    # new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)


# def test_update_header_first_group(app):
    # if app.group.count() == 0:
        # group_form = Group(name="Test group")
        # app.group.create(group_form)
    # old_groups = app.group.get_group_list()
    # group_form = Group(header="Updated Header")
    # app.group.update_first(group_form)
    # new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)
