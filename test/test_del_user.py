def test_del_first_user(app):
    app.user.delete_first_user(app, username="admin", password="secret")
