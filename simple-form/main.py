
import webapp2
from pages import Page  #import Page class from pages

class MainHandler(webapp2.RequestHandler):
    def get(self):

        if self.request.GET:  # if you can get these items then print this material
            first = self.request.GET['first']  # this is storing form info in a variable and then using that info for printing
            last = self.request.GET['last']   # this is storing form info in a variable and then using that info for printing
            email = self.request.GET['email']   # this is storing form info in a variable and then using that info for printing
            radio = self.request.GET['gender']   # this is storing form info in a variable and then using that info for printing
            check = self.request.GET['experience']   # this is storing form info in a variable and then using that info for printing
            select = self.request.GET['education']   # this is storing form info in a variable and then using that info for printing
            number = self.request.GET['quantity']   # this is storing form info in a variable and then using that info for printing
            self.response.write(first + ' ' + last + ' ' + email + ' ' + radio + ' ' + check + ' ' + select + ' ' + number) # this compiles all of the variable info from the form and prints it to the browser.
        else:
            p = Page()
            self.response.write(p.print_out())









app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
