from datetime import datetime


class Status:
    def __init__(self, status, webserver_status, webserver_status_created):
        self.status = status
        self.created = datetime.now()
        self.webserver_status = webserver_status
        self.webserver_status_created = webserver_status_created
