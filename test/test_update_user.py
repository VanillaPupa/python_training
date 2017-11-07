from model.user import User


def test_update_first_user(app):
    if app.user.count() == 0:
        contact = User(firstname="Sherlock", lastname="Holmes",
                       address="221b, Baker Street, London, UK", email="Sherlock@Museum.com",
                       email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355")
        app.user.add(contact)
        app.wd.get("http://localhost/addressbook/")
    contact = User(firstname="John H.", lastname="Watson", email="JohnH.Watson@Museum.com", email2="Dr.Watson@Museum.com")
    app.user.update_first(contact)
