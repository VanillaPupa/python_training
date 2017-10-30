# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.manager.create_group(username="admin", password="secret", name="Test group2", header="Header 4 test group2",
                             footer="Footer 4 test group2")


def test_create_empty_group(app):
    app.manager.create_group(username="admin", password="secret", name="", header="", footer="")