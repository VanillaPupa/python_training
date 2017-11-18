from model.user import User


def test_del_first_user(app):
    if app.user.count() == 0:
        contact = User(firstname="Sherlock", lastname="Holmes",
                       address="221b, Baker Street, London, UK", email="Sherlock@Museum.com",
                       email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355")
        app.user.add(contact)
        app.user.open_home_page()
    old_user_list = app.user.get_user_list()
    app.user.delete_first()
    new_user_list = app.user.get_user_list()
    assert len(old_user_list) - 1 == len(new_user_list)
    old_user_list[0:1] = []
    assert old_user_list == new_user_list
