# CSSI-Final
# Problem Statement
# Dog years measure the lifespans of our beloved canine companions. But what do we use to measure the life expectancy of our precious automobiles? We will build an app/website that calculates the “true” age of a car.
# Functional Requirements
# P0: Users can determine their ‘car’s age’ by inputting relevant spec.information: current car mileage, type of vehicle, driving habits (average miles/week), and manufacturing year and gives users recommendations for maintenance based on calculated ‘car age’.
# P1: Display user-submitted recommendations for maintenance based on ‘car age’ and expected car age.
# P2: Allows users to find highest rated repair shops in their area using maps.
# P3: Allow users to access a game with scores tracked via “timeline” / “leaderboard”



# Variables by Page

# Login Page

# Car Input Page

# Timeline Page

# Maintenance Recommendations Page

# Architecture

# Data

# V1


# class ShortUrl(ndb.Model):
  # label = ndb.StringProperty()
  # url = ndb.StringProperty()
  # views = ndb.IntegerProperty(default = 0)
  # creation_timestamp = ndb.DateTimeProperty(auto_now_add = True)
  # last_view_timestamp = ndb.DateTimeProperty()


# V2



# class ShortUrl(ndb.Model):
  # label = ndb.StringProperty()
  # url = ndb.StringProperty()
  # views = ndb.IntegerProperty(default = 0)
  # creation_timestamp = ndb.DateTimeProperty(auto_now_add = True)
  # last_view_timestamp = ndb.DateTimeProperty()

# class User(ndb.Model):
  # email = ndb.StringProperty(required = True)
  # user_id = ndb.StringProperty(required = True)
  # short_urls = ndb.KeyProperty(ShortUrl, repeated = True)

# User Experience and Mocks



# Handlers and Classes

# class LoginHandler (webapp2.RequestHandler):
    # def get(self):

# class InputHandler (webapp2.RequestHandler):
    # def post(self):


# class ResultHandler (webapp2.RequestHandler):
    # def get(self):

# class TimelineHandler (webapp2.RequestHandler):
    # def get(self):






# Project Timeline for Our Reference
# P0 and P1- Wednesday, July 24th, 2019
# → Login and Car Input Page Functioning by Tuesday at the latest
