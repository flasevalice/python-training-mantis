from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

    def can_login(self, username, password):
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        # список проектов для пользователя
        result = self.client.service.mc_projects_get_user_accessible(username, password)
        projects = list(map(lambda x: x.id, result))
        return projects
