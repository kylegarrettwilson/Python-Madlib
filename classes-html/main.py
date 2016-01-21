
import webapp2
from pages import Page  #import Page class from pages

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "My page!"
        p.css = "css/styles.css"
        p.update()
        self.response.write(p.whole_page)







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
