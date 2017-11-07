from model.group import Group


def test_create_group(app):
    group_form = Group(name="Test group", header="Header 4 group", footer="Footer 4 group")
    app.group.create(group_form)


def test_create_empty_group(app):
    group_form = Group(name="", header="", footer="")
    app.group.create(group_form)