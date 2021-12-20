from datetime import datetime


class Status:
    def __init__(self, status):
        self.status = status
        self.created = datetime.now()
