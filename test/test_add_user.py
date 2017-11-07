from model.user import User


def test_add_user(app):
    contact = User(firstname="Sherlock", lastname="Holmes",
                            address="221b, Baker Street, London, UK", email="Sherlock@Museum.com",
                            email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355")
    app.user.add(contact)