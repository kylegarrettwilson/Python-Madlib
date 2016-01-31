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

        employee1 = '<img src="' + d.people[0].image + '"><br>' + d.people[0].name + '<br>' + d.people[0].title + '<br>' + d.people[0].bio + '<br>' + d.people[0].email + '<br>' + d.people[0].phone + '<br>' + '$' + d.people[0].calc_wage() + ' Per appointment'
        employee2 = '<img src="' + d.people[1].image + '"><br>' + d.people[1].name + '<br>' + d.people[1].title + '<br>' + d.people[1].bio + '<br>' + d.people[1].email + '<br>' + d.people[1].phone + '<br>' + '$' + d.people[1].calc_wage() + ' Per appointment'
        employee3 = '<img src="' + d.people[2].image + '"><br>' + d.people[2].name + '<br>' + d.people[2].title + '<br>' + d.people[2].bio + '<br>' + d.people[2].email + '<br>' + d.people[2].phone + '<br>' + '$' + d.people[2].calc_wage() + ' Per appointment'
        employee4 = '<img src="' + d.people[3].image + '"><br>' + d.people[3].name + '<br>' + d.people[3].title + '<br>' + d.people[3].bio + '<br>' + d.people[3].email + '<br>' + d.people[3].phone + '<br>' + '$' + d.people[3].calc_wage() + ' Per appointment'
        employee5 = '<img src="' + d.people[4].image + '"><br>' + d.people[4].name + '<br>' + d.people[4].title + '<br>' + d.people[4].bio + '<br>' + d.people[4].email + '<br>' + d.people[4].phone + '<br>' + '$' + d.people[4].calc_wage() + ' Per appointment'

        if self.request.GET:
            user = self.request.GET['user']
            if user == 'carl':
                c.inputs = (employee1)
                self.response.write(c.print_now2())

        if self.request.GET:
            user = self.request.GET['user']
            if user == 'roy':
                c.inputs = (employee2)
                self.response.write(c.print_now2())

        if self.request.GET:
            user = self.request.GET['user']
            if user == 'ned':
                c.inputs = (employee3)
                self.response.write(c.print_now2())

        if self.request.GET:
            user = self.request.GET['user']
            if user == 'pete':
                c.inputs = (employee4)
                self.response.write(c.print_now2())

        if self.request.GET:
            user = self.request.GET['user']
            if user == 'heather':
                c.inputs = (employee5)
                self.response.write(c.print_now2())

        else:
            self.response.write(c.print_now1())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
