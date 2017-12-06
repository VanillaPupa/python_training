from model.group import Group
import pytest
import random
import string


def random_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + ": " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata_updated = [Group(name="", header="", footer="")] + \
                   [Group(name=random_str("name", 10), header="", footer="")] + \
                   [Group(name="", header=random_str("header", 20), footer="")] + \
                   [Group(name="", header="", footer=random_str("footer", 20))] + \
                   [Group(name=random_str("name", 10), header=random_str("header", 20), footer=random_str("footer", 20))
                    for i in range(5)]

testdata_new = [Group(name=random_str("name", 10), header=random_str("header", 20),
                  footer=random_str("footer", 20))]


@pytest.mark.parametrize("new_group_form", testdata_new, ids=[repr(x) for x in testdata_new])
@pytest.mark.parametrize("updated_group_form", testdata_updated, ids=[repr(x) for x in testdata_updated])
def test_update_some_group(app, new_group_form, updated_group_form):
    if app.group.count() == 0:
        app.group.create(new_group_form)
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    updated_group_form.id = old_groups[index].id
    app.group.update_by_index(index, updated_group_form)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = updated_group_form
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
