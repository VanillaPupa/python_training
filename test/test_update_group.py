from model.group import Group


def test_update_first_group(app):
    group_form = Group(name="Updated group", header="Updated Header 4 group", footer="Updated Footer 4 group")
    app.group.update_first_group(app, group_form, username="admin", password="secret")


def test_update_name_first_group(app):
    group_form = Group(name="Updated Name")
    app.group.update_first_group(app, group_form, username="admin", password="secret")


def test_update_header_first_group(app):
    group_form = Group(header="Updated Header")
    app.group.update_first_group(app, group_form, username="admin", password="secret")
