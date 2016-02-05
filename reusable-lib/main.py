
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


class MainHandler(webapp2.RequestHandler):   # main handler class for connecting everything together
    def get(self):

        f = FormPage()  # variable for form page class
        f.css = "css/styles.css"   # this is the css file for styling
        r = ResultsPage()  # variable for results page class


        if self.request.GET:  # this is an if else statement so ensure the right html is printed
            jb1 = JobData()  # creating an instance
            jb1.name = self.request.GET['last']  # getting the data from the form
            jb1.hours = self.request.GET['hours']  # getting the data from the form
            jb1.pay = self.request.GET['pay']  # getting the data from the form
            jb1.over = self.request.GET['over']  # getting the data from the form
            jb1.calc_check()  # calling the check amount from the library page
            jb1.over_time()   # calling the over time amount from library page
            jb1.total_time()  # calling the total time worked from the library page
            jb1.bonus()   # calling the bonus qualification from the library page
            r.body = 'Total check amount: ' + jb1.calc_check() + '<br>' + 'Total overtime amount: ' + jb1.over_time() + '<br>' + 'Average hours worked per week: ' + jb1.total_time() + '<br>' + jb1.bonus() + '<br>' + 'Last Name: ' + jb1.name + '<br>' + 'Hours worked: ' + jb1.hours + '<br>' + 'Pay per hour: ' + jb1.pay + '<br>' + 'Overtime: ' + jb1.over  # printing the results from the library calculations and the user entered amounts to the body tag so it is all within the html document
            self.response.write(r.print_out_second())  # this is printing one of the html pages to the window
        else:  # if there are no items entered by the user, print this
            self.response.write(f.print_out())   # print the form page
































app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
