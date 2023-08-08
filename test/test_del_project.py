from model.project import Project
import random
import pytest
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(project_name=random_string("project", 10), project_description=random_string("descr", 10))
    for i in range(2)
]


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_del_project(app, project):
    app.session.login("administrator", "root")
    if len(app.soap.get_projects_list()) == 0:
        app.project.create(project)
    old_projects_list = app.soap.get_projects_list()
    project_rnd = random.choice(old_projects_list)
    app.project.delete_project(project_rnd)
    new_projects_list = app.soap.get_projects_list()
    old_projects_list.remove(project_rnd)
    assert sorted(old_projects_list, key=Project.name_or_empty) == sorted(new_projects_list, key=Project.name_or_empty)
    app.session.logout()
