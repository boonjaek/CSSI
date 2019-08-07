import webapp2
import logging
from google.appengine.api import urlfetch
from data_model import key_data
import json
import jinja2
import os


from google.appengine.api import users
from google.appengine.ext import ndb
# from api import CarmdApi
# api = CarmdApi()

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape="true")

def GetProcedure(description, data):
    for procedure in data:
        if procedure["desc"] == description:
            return procedure["desc"], procedure["repair"]["repair_hours"], procedure["repair"]["total_cost"], procedure["repair"]["repair_difficulty"]

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        user = users.get_current_user()
        signout_link_html = users.create_logout_url('/')

        cssi_dictionary = {
          "signout_link_html": signout_link_html,
        };
        input_template = the_jinja_env.get_template('templates/input.html')
        self.response.write(input_template.render(cssi_dictionary))  # the response
    # def post(self):
    def post(self):  # for a get request
        user = users.get_current_user()
        signout_link_html = users.create_logout_url('/')

        cssi_dictionary = {
          "signout_link_html": signout_link_html,
        };
        input_template = the_jinja_env.get_template('templates/input.html')
        self.response.write(input_template.render(cssi_dictionary))  # the response
    # def post(self):

class ShowInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/input.html')
        self.response.write(welcome_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('templates/output.html')
        # try:
        if float(self.request.get("Mileage")).is_integer() is True:
            Age = (float(self.request.get("Mileage"))/200000)*80.3

            Year = self.request.get("Year")
            Make = self.request.get("Make")
            Model = self.request.get("Model")
            Mileage = self.request.get("Mileage")

            if int(Year) < 1996:
                self.response.write("Please enter a year after 1994.")
                return

            first_key = key_data.query().get()


            API = "http://api.carmd.com/v3.0/maint?year=%s&make=%s&model=%s&mileage=%s" %(Year, Make, Model, Mileage)
            header = {"content-type":"application/json",
                        "authorization":first_key.authKey,
                        "partner-token":first_key.parTok}
            print header
            print API
            response = urlfetch.fetch(url=API, headers=header).content
            json_response = json.loads(response)
            datalist =[
                item for item in json_response["data"]
                if item["repair"]["repair_hours"] != 0.00 or item["repair"]["total_cost"] != 0.00 or item["repair"]["repair_difficulty"] != 0
            ]

            the_variable_dict = {
                                "carAge": Age,
                                "datalist": datalist,
                                }

            self.response.write(results_template.render(the_variable_dict))
        # except:
            self.response.write('''
                Please input an integer value and a valid Car Entry!
                <p> Click below to Calculate the Age of your Car! </p>
                  <form method="post" action="/enter-info">
                    <input type="submit" value="Go!">
                    </input>
                  </form>''')
    # TestFunction()
#
# app = webapp2.WSGIApplication([
#     ('/EnterInfo', EnterInfoHandler),
#     ('/carResult', ShowInfoHandler),
# ], debug="true")

#
# # buried code:
#     # if Age <= 1:
#     #     info_dict = {"info": "Katie"}
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Infancy
#     # elif Age <= 8:
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Childhood
#     # elif Age <= 13:
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Puberty
#     # elif Age <= 18:
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Adolescence
#     # elif Age <= 31:
#     #     the_variable_dict.update(info = 'Katie')
#     #
#     #
#     #     # Adulthood
#     # elif Age <= 50:
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Middle Age
#     # else:
#     #     self.response.write(results_template.render(info_dict))
#     #     #
#     #     # Old Age
#     #
#     #     def Merge(the_variable_dict, info_dict):
#     #         return(info_dict.update(the_variable_dict))
