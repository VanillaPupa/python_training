from model.user import User


def test_update_first_user(app):
    contact = User(firstname="John H.", lastname="Watson", email="JohnH.Watson@Museum.com", email2="Dr.Watson@Museum.com")
    app.user.update_first(contact)
