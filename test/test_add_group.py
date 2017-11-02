from model.group import Group


def test_create_group(app):
    group_form = Group(name="Test group", header="Header 4 group", footer="Footer 4 group")
    app.group.create_group(app, group_form, username="admin", password="secret")


def test_create_empty_group(app):
    group_form = Group(name="", header="", footer="")
    app.group.create_group(app, group_form, username="admin", password="secret")
