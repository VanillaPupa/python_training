# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.user import User


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.add(User(firstname="Sherlock", lastname="Holmes", address="221b, Baker Street, London, UK",
                      email="Sherlock@Museum.com", email2="Holmes@Museum.com", hometel="3213213", mobiletel="+441712223355"))
    app.session.logout()