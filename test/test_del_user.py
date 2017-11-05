def test_del_first_user(app):
    app.user.delete_first()
