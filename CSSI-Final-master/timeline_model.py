from google.appengine.ext import ndb

class timeline_data(ndb.Model):
    carAge =  ndb.StringProperty(required=True)
    email =  ndb.StringProperty(required=True)
    year =  ndb.StringProperty(required=True)
    make =  ndb.StringProperty(required=True)
    model =  ndb.StringProperty(required=True)
# could do Integer
