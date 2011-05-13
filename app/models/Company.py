from google.appengine.ext import db

class Company(db.Model):
    name = db.StringProperty(required=True)

    def __init__(self):
        # For debugging purposes, let's have google
        # already defined in the database.
        query = Company.get_by_key_name("google")
        if query == None:
            company = Company(name="google")
            company.put()