
# Kyle Wilson
# Reusable Library
# 1-21-16

# this will contain the print out to the window
# this will route the information as to where it needs to go
# this will import and connect all of the data together




import webapp2
from page import FormPage
from page import ResultsPage
from library import JobData


class MainHandler(webapp2.RequestHandler):
    def get(self):

        f = FormPage()
        r = ResultsPage()

        if self.request.GET:
            jb1 = JobData()
            jb1.name = self.request.GET['last']
            jb1.hours = self.request.GET['hours']
            jb1.pay = self.request.GET['pay']
            jb1.over = self.request.GET['over']
            self.response.write(r.print_out_second() + jb1.name + jb1.hours + jb1.pay + jb1.over)
        else:
            self.response.write(f.print_out())
































app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
