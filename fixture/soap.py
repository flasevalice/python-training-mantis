from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        base_url = self.app.config['web']['baseUrl']
        client = Client(base_url + "mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        base_url = self.app.config['web']['baseUrl']
        client = Client(base_url + "mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            # список проектов для пользователя
            projects = client.service.mc_projects_get_user_accessible(username, password)
            project_list = []
            for project in projects:
                project_list.append(Project(project_id=project.id,
                                            project_name=project.name,
                                            project_description=project.description))
            return project_list
        except WebFault:
            return None
