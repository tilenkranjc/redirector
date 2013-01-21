from google.appengine.ext import db

class Urls(db.Model):
	
	name = db.StringProperty()
	shorturl = db.StringProperty()
	url = db.StringProperty()
	date = db.DateTimeProperty(auto_now_add=True)
	author = db.StringProperty()
	
