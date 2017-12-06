from model.group import Group
import pytest
import random
import string


def random_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + ": " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + \
           [Group(name=random_str("name", 10), header=random_str("header", 20),
                  footer=random_str("footer", 20)) for i in range(5)]


@pytest.mark.parametrize("group_form", testdata, ids=[repr(x) for x in testdata])
def test_create_group(app, group_form):
    old_groups = app.group.get_group_list()
    app.group.create(group_form)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group_form)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
