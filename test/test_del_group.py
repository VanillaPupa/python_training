from model.group import Group
import pytest
import random
import string


def random_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name=random_str("name", 10), header=random_str("header", 20),
                  footer=random_str("footer", 20))]


@pytest.mark.parametrize("group_form", testdata, ids=[repr(x) for x in testdata])
def test_del_some_group(app, group_form):
    if app.group.count() == 0:
        app.group.create(group_form)
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    app.group.delete_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
