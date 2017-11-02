def test_del_first_group(app):
    app.group.delete_first_group(app, username="admin", password="secret")
