from model.group import Group
from data.add_group import constant as testdata
import pytest


@pytest.mark.parametrize("group_form", testdata, ids=[repr(x) for x in testdata])
def test_create_group(app, group_form):
    old_groups = app.group.get_group_list()
    app.group.create(group_form)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group_form)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

