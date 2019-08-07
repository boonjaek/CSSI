from google.appengine.ext import ndb

class key_data(ndb.Model):
    parTok =  ndb.StringProperty(required=True)
    authKey =  ndb.StringProperty(required=True)

# could do Integer
