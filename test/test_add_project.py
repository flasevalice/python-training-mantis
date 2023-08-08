from model.project import Project
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(project_name=random_string("project", 10), project_description=random_string("descr", 10))
    for i in range(2)
]


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    app.session.login("administrator", "root")
    old_projects_list = app.soap.get_projects_list()
    app.project.add_new_project(project)
    app.session.logout()
    new_projects_list = app.soap.get_projects_list()
    assert len(old_projects_list)+1 == len(new_projects_list)
    old_projects_list.append(project)
    assert sorted(old_projects_list, key=Project.name_or_empty) == sorted(new_projects_list, key=Project.name_or_empty)

