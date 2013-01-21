import jinja2
import os
import webapp2
from datetime import datetime
from google.appengine.ext import db
from google.appengine.api import users

from models import Urls

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
	jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
	
class BaseHandler(webapp2.RequestHandler):
	
	@webapp2.cached_property
	def jinja2(self):
		return jinja2.get_jinja2(app=self.app)
		
	def render_template(self, filename, template_values, **template_args):
		template = jinja_environment.get_template(filename)
		self.response.out.write(template.render(template_values))
		
		
class MainPage(BaseHandler):
	
	def get(self):
		urls = Urls.all()
		self.render_template('index.htm',{'urls':urls})
		
class Redirect(BaseHandler):
	
	def get(self, shorturl):
		urls = db.Query(Urls)
		#urls = db.Query(Urls, projection=('shorturl','url'))
		urls.filter('shorturl =',shorturl)
		result = urls.get()
		return webapp2.redirect(str(result.url))
		
		
class AddUrl(BaseHandler):
	
	def post(self):
		author1 = users.get_current_user().nickname()
		url = Urls(name=self.request.get('name'),
					shorturl=self.request.get('shorturl'),
					url=self.request.get('url'),
					author=author1)
		url.put()
		return webapp2.redirect('/')
		
	def get(self):
		self.render_template('add.htm','')
		#return webapp2.redirect('/')
		

class EditUrl(BaseHandler):
	
	def post(self, url_id):
		iden = int(url_id)
		url = db.get(db.Key.from_path('Urls', iden))
		url.author = users.get_current_user().nickname()
		url.name = self.request.get('name')
		url.shorturl=self.request.get('shorturl')
		url.url=self.request.get('url')
		url.date = datetime.now()
		url.put()
		return webapp2.redirect('/')
		
	def get(self, url_id):
		iden = int(url_id)
		url = db.get(db.Key.from_path('Urls',iden))
		self.render_template('edit.htm', {'url':url})
		

class DeleteUrl(BaseHandler):
	
	def get(self, url_id):
		iden = int(url_id)
		url = db.get(db.Key.from_path('Urls', iden))
		db.delete(url)
		return webapp2.redirect('/')
	
	
	
