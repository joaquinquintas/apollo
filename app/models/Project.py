from google.appengine.ext import db

class Project(db.Model):
    name = db.StringProperty(required=True)

    def __init__(self):
        pass
