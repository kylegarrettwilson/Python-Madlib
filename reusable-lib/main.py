
# Kyle Wilson
# Reusable Library
# 1-21-16

# this will contain the print out to the window
# this will route the information as to where it needs to go
# this will import and connect all of the data together




import webapp2
from page import FormPage
from page import ResultsPage


class MainHandler(webapp2.RequestHandler):
    def get(self):

        f = FormPage()
        r = ResultsPage()



        if self.request.GET:
            name = self.request.GET['last']
            hours = self.request.GET['hours']
            pay = self.request.GET['pay']
            over = self.request.GET['over']
            self.response.write(name + hours + pay + over)
        else:
            self.response.write(f.print_out())
































app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
