from model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        group_form = Group(name="Test group")
        app.group.create(group_form)
    app.group.delete_first()
