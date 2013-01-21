import webapp2
from views import MainPage, Redirect, AddUrl, DeleteUrl, EditUrl


app = webapp2.WSGIApplication([
		webapp2.Route(r'/', handler=MainPage, name='MainPage'),
		webapp2.Route(r'/add', handler=AddUrl, name='AddUrl'),
		webapp2.Route(r'/del/<url_id>', handler=DeleteUrl, name='DeleteUrl'),
		webapp2.Route(r'/edit/<url_id>', handler=EditUrl, name='EditUrl'),
		webapp2.Route(r'/<shorturl>', handler=Redirect, name='Redirect')
		],
		debug=True)
