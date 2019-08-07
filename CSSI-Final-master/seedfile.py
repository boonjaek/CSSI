import webapp2
import jinja2
import os
import urllib
import urllib2
import json
import logging
from data_model import key_data

class inputData(webapp2.RequestHandler):
    def get(self):
        data_input = key_data(parTok="0dab2fa8f63540548c92b957017b2e6c", authKey = "Basic NmNiNGNmN2YtZGRiNS00OWFmLWIyZmYtNzNmYWZkNTMxZDE1")
        timelinedata = data_input.put()



    def post(self):
        data_input = key_data(parTok="0dab2fa8f63540548c92b957017b2e6c", authKey = "Basic NmNiNGNmN2YtZGRiNS00OWFmLWIyZmYtNzNmYWZkNTMxZDE1")
        timelinedata = data_input.put()
