# Kyle Wilson
# 1-29-16
# Dynamic Website




import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

























app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
