import webapp2
import jinja2
import os
from timeline_model import timeline_data
from data_model import key_data

from google.appengine.api import users
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class inputTimeline(webapp2.RequestHandler):
  def get(self):
      user = users.get_current_user()

      signout_link_html = users.create_logout_url('/')

      cssi_dictionary = {
        "signout_link_html": signout_link_html,
      };
      timeline_template = jinja_env.get_template("templates/inputTimeline.html")
      self.response.write(timeline_template.render(cssi_dictionary))




class displayTimeline(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        the_carage = self.request.get("carage")
        the_year = self.request.get("year")
        the_make = self.request.get("Make")
        the_model = self.request.get("Model")
        timeline_input = timeline_data(carAge= the_carage,email= email_address, year = the_year, make = the_make, model = the_model)
        timelinedata = timeline_input.put()


    def post(self):
        the_carage = self.request.get("carage")
        the_year = self.request.get("Year")
        the_make = self.request.get("Make")
        the_model = self.request.get("Model")

        user = users.get_current_user()
        email_address = user.nickname()
        signout_link_html = users.create_logout_url('/')



        timeline_input = timeline_data(carAge= the_carage, email= email_address, year = the_year, make = the_make, model = the_model)
        timelinedata = timeline_input.put()
        timeline_entity_list = timeline_data.query().order(timeline_data.carAge).fetch()
        new_entity = timelinedata.get()
        timeline_entity_list.append(new_entity)
        cssi_dictionary = {
        "signout_link_html": signout_link_html,
        'timeline_info' : timeline_entity_list,
        };

        timeline_template = jinja_env.get_template("templates/timeline.html")
        self.response.write(timeline_template.render(cssi_dictionary))
