import pytest

from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_del_first_group(app):
    app.group.delete_first_group(username="admin", password="secret")