
# Kyle Wilson
# Reusable Library
# 1-21-16

# this will contain the print out to the window
# this will route the information as to where it needs to go
# this will import and connect all of the data together




import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):































app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
