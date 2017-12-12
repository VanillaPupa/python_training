from model.group import Group
# import pytest
import random
# import string


# def random_str(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#     return prefix + ": " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata = [Group(name=random_str("name", 10), header=random_str("header", 20),
#                   footer=random_str("footer", 20))]


# @pytest.mark.parametrize("group_form", testdata, ids=[repr(x) for x in testdata])
def test_del_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name4del"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # index = random.randrange(len(old_groups))
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
