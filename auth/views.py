class ServiceLayer(object):
    def __init__(self, cli):
        self.cli = cli

    def add_session(self, username, password, role):
        try:
            status, session_id = self.cli.add_session(
                username=username, password=password, role=role
            )
            return status, session_id

        except BaseException:
            return 500, ""

    def delete_session(self, session_id):
        try:
            status, s_id = self.cli.delete_session(session_id)
            return status, s_id

        except BaseException:
            return 500, ""

    def get_session(self, session_id):
        try:
            status, user = self.cli.get_session(session_id)
            if status == 201:
                return status, user.role
            elif status == 404:
                return status, "Not logged in"

        except BaseException:
            return 500
