from google.appengine.ext import db

class Company(db.Model):
    name = db.StringProperty(required=True)

    def __init__(self):
        pass
