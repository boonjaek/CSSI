import webapp2
import jinja2
import os
import urllib
import urllib2
import json
import logging


from timeline import inputTimeline, displayTimeline
from timeline_model import timeline_data
from seedfile import inputData
from caragecalc import EnterInfoHandler, ShowInfoHandler
from google.appengine.api import users
from google.appengine.ext import ndb


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class CssiUser(ndb.Model):
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  email = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    # If the user is logged in...
    if user:
      signout_link_html = users.create_logout_url('/')
      signout_link_htmll = '<a href="%s"> Sign Out</a>' %(users.create_logout_url('/'))
      email_address = user.nickname()
      cssi_user = CssiUser.query().filter(CssiUser.email == email_address).get()
      # If the user is registered...
      if cssi_user:
        # Greet them with their personal information
        cssi_dictionary = {
          "signout_link_html": signout_link_html,
        };
        cssi_template = the_jinja_env.get_template("templates/autoSpanhome.html")
        self.response.write(cssi_template.render(cssi_dictionary));


      # If the user isn't registered...
      else:
        # Offer a registration form for a first-time visitor:
        self.response.write('''
                <head>
                <link rel="stylesheet" type="text/css" href="../static/autoSpanregistration.css">
                <link href="https://fonts.googleapis.com/css?family=Poppins&display=swap" rel="stylesheet">
            </head>

            <body>


            <img src="https://i.imgur.com/Oooxo1B.png" alt="car placeholder" id=regPlaceholder>
            <div id="registerBox">
            <p><h1 id=welcoming> Welcome to VroomIQ , %s. It appears you are not already registered for our site. If you would like to continue, please fill out the form found below.</h1> </p> <br>
                <ul>
                    <form method="post" action="/" class="registrationForm">
                    <li><input type="text" name="first_name" value="First Name"> </li>
                    <li><input type="text" name="last_name" value="Last Name"> </li>
                    <li><h1 id=submitButton><input type="submit"></h1></li>
                    </form>

                </ul>
                <br> <h1 id=signoutButton> %s </h1> <br>
            </div>
            </body>

            ''' % (email_address, signout_link_htmll))



    else:
      # If the user isn't logged in...
      print("Hello.")
      login_url = users.create_login_url('/')
      login_template = the_jinja_env.get_template("templates/autoSpanlogin.html")
      login_html_element = '<a href="%s">Sign in</a>' % login_url
      variable_dictionary = {
        "login_url": login_url,
      };

      # Prompt the user to sign in.
      self.response.write(login_template.render(variable_dictionary));

  def post(self):
    # Code to handle a first-time registration from the form:
    user = users.get_current_user()
    cssi_user = CssiUser(
        first_name=self.request.get('first_name'),
        last_name=self.request.get('last_name'),
        email=user.nickname())
    cssi_user.put()
    self.response.write("templates/autoSpanhome.html")

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ("/input-timeline", inputTimeline),
  ("/display", displayTimeline),
  ("/enter-info", EnterInfoHandler),
  ("/show-info", ShowInfoHandler),
  ("/seed-data", inputData),
], debug=True)
