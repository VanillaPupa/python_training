import re


def test_phones_on_home_page(app):
    index = 0
    user_from_home_page = app.user.get_user_list()[index]
    user_from_edit_page = app.user.get_user_info_from_edit_page(index)
    assert user_from_home_page.all_phones_frome_home_page == merge_phones_like_on_home_page(user_from_edit_page)


def test_phones_on_user_view_page(app):
    index = 0
    user_from_view_page = app.user.get_user_info_from_view_page(index)
    user_from_edit_page = app.user.get_user_info_from_edit_page(index)
    assert user_from_view_page.homephone == user_from_edit_page.homephone
    assert user_from_view_page.workphone == user_from_edit_page.workphone
    assert user_from_view_page.mobilephone == user_from_edit_page.mobilephone
    assert user_from_view_page.additionalphone == user_from_edit_page.additionalphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.homephone, user.mobilephone, user.workphone, user.additionalphone]))))
