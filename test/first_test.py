def test_create_group(app):
    app.group.create_group(username="admin", password="secret", name="Test group", header="Header 4 test group2",
                             footer="Footer 4 test group2")


def test_create_empty_group(app):
    app.group.create_group(username="admin", password="secret", name="", header="", footer="")