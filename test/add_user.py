def test_add_user(app):
    app.user.create_user(app, username="admin", password="secret", firstname="Sherlock", lastname="Holmes",
                            address="221b, Baker Street, London, UK", email="Sherlock@Museum.com",
                            email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355")