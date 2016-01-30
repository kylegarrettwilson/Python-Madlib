

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['first_name', 'text', 'First Name'],['last_name', 'text', 'Last Name'],['Submit', 'submit']]
        self.response.write(p.print_out_form())


class Page(object):  #borrowing stuff from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title> </title>
    <body>'''

        self._body = 'Filler'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close





class FormPage(Page): # this is inheriting from page class
    def __init__(self): # constructor for this class
        #constructor function for super class
        super(FormPage, self).__init__()

        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self.__form_inputs = ''
        # <input type="text" value="" name= "" />


    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, ar):
        #change my private inputs variable and make html
        self.__inputs = ar
        for item in ar:
            self.__form_inputs += '<input type="' + item[1] + '"' + '" name="' + item[0]
            try:
                self.__form_inputs += '" placeholder="' + item[2] + '" />'
            except:
                self.__form_inputs += '" />'



    def print_out_form(self):
        return self._head + self._body + self._form_open + self.__form_inputs + self._form_close + self._close































app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
