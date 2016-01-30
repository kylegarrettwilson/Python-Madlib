# Kyle Wilson
# 1-29-16
# Dynamic Website




import webapp2
from data import Employee
from data import Data
from page import Page
from page import ContentPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = ContentPage()
        d = Data()

        employee1 = d.people[0].title + d.people[0].name + d.people[0].bio + d.people[0].email + d.people[0].image + d.people[0].phone
        employee2 = d.people[1].title + d.people[1].name + d.people[1].bio + d.people[1].email + d.people[1].image + d.people[1].phone
        employee3 = d.people[2].title + d.people[2].name + d.people[2].bio + d.people[2].email + d.people[2].image + d.people[2].phone
        employee4 = d.people[3].title + d.people[3].name + d.people[3].bio + d.people[3].email + d.people[3].image + d.people[3].phone
        employee5 = d.people[4].title + d.people[4].name + d.people[4].bio + d.people[4].email + d.people[4].image + d.people[4].phone


        if self.request.GET('carl'):
            worker = d.people('carl')
            self.response.write((c.print_now() + employee1))

        elif self.request.GET('roy'):
            worker = d.people('roy')
            self.response.write((c.print_now() + employee2))

        elif self.request.GET('ned'):
            worker = d.people('ned')
            self.response.write((c.print_now() + employee3))

        elif self.request.GET('pete'):
            worker = d.people('pete')
            self.response.write((c.print_now() + employee4))

        elif self.request.GET('heather'):
            worker = d.people('heather')
            self.response.write((c.print_now() + employee5))

        else:
            self.response.write(c.print_now())






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
