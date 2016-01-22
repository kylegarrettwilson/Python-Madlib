
# Kyle Wilson
# Reusable Library
# 1-21-16

# this will contain the print out to the window
# this will route the information as to where it needs to go
# this will import and connect all of the data together

# I know I can put commas between the imports from the same page but I was able to better visualize it this way

# importing all of the classes from the various files
import webapp2
from page import FormPage
from page import ResultsPage
from library import JobData
from library import PayStub


class MainHandler(webapp2.RequestHandler):   # main handler class for connecting everything together
    def get(self):

        f = FormPage()  # variable for form page class
        r = ResultsPage()  # variable for results page class
        pay = PayStub()  # variable for the paystub class

        if self.request.GET:  # this is an if else statement so ensure the right html is printed
            jb1 = JobData()  # creating an instance
            jb1.name = self.request.GET['last']  # getting the data from the form
            jb1.hours = self.request.GET['hours']  # getting the data from the form
            jb1.pay = self.request.GET['pay']  # getting the data from the form
            jb1.over = self.request.GET['over']  # getting the data from the form
            pay.add_check(jb1)  # calling the add check function
            pay.calc_check()  # calling the function
            pay.over_time()   # calling the function
            r.body = pay.calc_check() + pay.over_time()   # printing the results from the two calcs to the body tag
            self.response.write(r.print_out_second() + jb1.name + jb1.hours + jb1.pay + jb1.over)  # printing to window
        else:
            self.response.write(f.print_out())   # or else printing the form
































app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
