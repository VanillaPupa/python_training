# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="Test group2", header="Header 4 test group2", footer="Footer 4 test group2"))
    app.logout()


def test_create_empty_group(app):
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


if __name__ == '__main__':
    unittest.main()
