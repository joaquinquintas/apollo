#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from app.controllers.MainHandler import MainHandler
from app.controllers.SignupHandler import SignupHandler
from app.controllers.CompanyHandler import CompanyHandler
from app.controllers.ProjectController import ProjectController

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# Put route information here
router = [
    ('/', MainHandler),
    ('/projects', ProjectController),
    ('/company', CompanyHandler),
    ('/signup', SignupHandler)
]

def main():
    application = webapp.WSGIApplication(
        router,
        debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
