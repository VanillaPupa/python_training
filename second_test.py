# -*- coding: utf-8 -*-
import pytest
from user import User
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.login(username="admin", password="secret")
    app.add_user(User(firstname="Sherlock", lastname="Holmes", address="221b, Baker Street, London, UK",
                 email="Sherlock@Museum.com", email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355"))
    app.logout()


if __name__ == '__main__':
    unittest.main()
