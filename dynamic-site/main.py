# Kyle Wilson
# 1-29-16
# Dynamic Website




import webapp2
from data import Employee
from data import Data
from page import Page
from page import LinkPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = LinkPage()
        d = Data()

        employee1 = d.people[0].title + d.people[0].bio + d.people[0].email + d.people[0].image + d.people[0].phone
        employee2 = d.people[1].title + d.people[1].bio + d.people[1].email + d.people[1].image + d.people[1].phone
        employee3 = d.people[2].title + d.people[2].bio + d.people[2].email + d.people[2].image + d.people[2].phone
        employee4 = d.people[3].title + d.people[3].bio + d.people[3].email + d.people[3].image + d.people[3].phone
        employee5 = d.people[4].title + d.people[4].bio + d.people[4].email + d.people[4].image + d.people[4].phone


        if self.request.GET:
            name = self.request.GET('carl')
            self.response.write((c.print_now() + name + employee1))

        elif self.request.GET:
            name = self.request.GET('roy')
            self.response.write((c.print_now() + name + employee2))

        elif self.request.GET:
            name = self.request.GET('ned')
            self.response.write((c.print_now() + name + employee3))

        elif self.request.GET:
            name = self.request.GET('pete')
            self.response.write((c.print_now() + name + employee4))

        elif self.request.GET:
            name = self.request.GET('heather')
            self.response.write((c.print_now() + name + employee5))

        else:
            self.response.write(c.print_now())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
