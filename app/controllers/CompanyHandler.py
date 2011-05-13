import os
import cgi

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp

from app.models.Company import Company

class CompanyHandler(webapp.RequestHandler):
    def get(self):
        name = cgi.escape(self.request.get('name'))
        query = Company.get_by_key_name(name)
        if query == None:
            self.response.out.write("False")
        else:
            self.response.out.write("True")