# Kyle Wilson
# 1-29-16
# Dynamic Website


import webapp2
from data import Employee     # importing a class
from data import Data    # importing a class
from page import Page   # importing a class
from page import LinkPage    # importing a class


class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = LinkPage()   # invoking the link page class
        d = Data()   # invoking the data class

         # these are the variables that I am using to organize the data class info and make sure it prints out the right info per employee
        employee1 = '<img src="' + d.people[0].image + '"><br>' + d.people[0].name + '<br>' + d.people[0].title + '<br>' + d.people[0].bio + '<br>' + d.people[0].email + '<br>' + d.people[0].phone + '<br>' + '$' + d.people[0].calc_wage() + ' Per appointment'
        employee2 = '<img src="' + d.people[1].image + '"><br>' + d.people[1].name + '<br>' + d.people[1].title + '<br>' + d.people[1].bio + '<br>' + d.people[1].email + '<br>' + d.people[1].phone + '<br>' + '$' + d.people[1].calc_wage() + ' Per appointment'
        employee3 = '<img src="' + d.people[2].image + '"><br>' + d.people[2].name + '<br>' + d.people[2].title + '<br>' + d.people[2].bio + '<br>' + d.people[2].email + '<br>' + d.people[2].phone + '<br>' + '$' + d.people[2].calc_wage() + ' Per appointment'
        employee4 = '<img src="' + d.people[3].image + '"><br>' + d.people[3].name + '<br>' + d.people[3].title + '<br>' + d.people[3].bio + '<br>' + d.people[3].email + '<br>' + d.people[3].phone + '<br>' + '$' + d.people[3].calc_wage() + ' Per appointment'
        employee5 = '<img src="' + d.people[4].image + '"><br>' + d.people[4].name + '<br>' + d.people[4].title + '<br>' + d.people[4].bio + '<br>' + d.people[4].email + '<br>' + d.people[4].phone + '<br>' + '$' + d.people[4].calc_wage() + ' Per appointment'

        if self.request.GET:  # this is an if statement that gets the variable from the url
            user = self.request.GET['user']   # if there is an item user in the url
            if user == 'carl':  # and it is equal to carl
                c.inputs = (employee1)  # print employee one from above
                self.response.write(c.print_now2())  # and attach it to the second print out function

        if self.request.GET:   # this is an if statement that gets the variable from the url
            user = self.request.GET['user']  # if there is an item user in the url
            if user == 'roy':   # and it is equal to roy
                c.inputs = (employee2)  # print employee two from above
                self.response.write(c.print_now2())  # and attach it to the second print out function

        if self.request.GET:   # this is an if statement that gets the variable from the url
            user = self.request.GET['user']   # if there is an item user in the url
            if user == 'ned':   # and it is equal to ned
                c.inputs = (employee3)  # print employee three from above
                self.response.write(c.print_now2())  # and attach it to the second print out function

        if self.request.GET:    # this is an if statement that gets the variable from the url
            user = self.request.GET['user']  # if there is an item user in the url
            if user == 'pete':    # and it is equal to pete
                c.inputs = (employee4)  # print employee four from above
                self.response.write(c.print_now2())  # and attach it to the second print out function

        if self.request.GET:    # this is an if statement that gets the variable from the url
            user = self.request.GET['user']   # if there is an item user in the url
            if user == 'heather':   # and it is equal to heather
                c.inputs = (employee5)  # print employee five from above
                self.response.write(c.print_now2())  # and attach it to the second print out function

        else:
            self.response.write(c.print_now1())    #else print out the first print out from page class


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
