from model.user import User


def test_del_first_user(app):
    if app.user.count() == 0:
        contact = User(firstname="Sherlock", lastname="Holmes",
                       address="221b, Baker Street, London, UK", email="Sherlock@Museum.com",
                       email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355")
        app.user.add(contact)
        app.wd.get("http://localhost/addressbook/")
    app.user.delete_first()
