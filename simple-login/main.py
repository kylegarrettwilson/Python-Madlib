'''
Kyle Wilson
1-14-16
DPW
Simple Login Form
'''







import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):

        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
    <title></title>



    </head>
    <body>'''





        page_body = '''<form method="GET">
            <label>First Name: </label><input type="text" name="first" />
            <label>Last Name: </label><input type="text" name="last" />
            <label>Email: </label><input type="email" name="email" />
            <input type="radio" name="gender" value="male" checked>Male
            <br>
            <input type="radio" name="gender" value="female">Female
            <br>
            <input type="radio" name="experience" value="yes" checked>I have a currently have a job
            <br>
            <input type="radio" name="experience" value="no">I do not currently have a job
            <br>
            <select name="education">
                <option value="doctoral">I have a Phd</option>
                <option value="masters">I have a Masters degree</option>
                <option value="bachelors">I have a Bachelors degree</option>
                <option value="associates">I have an Associates degree</option>
                <option value="nodegree">I do not have a college degree</option>
            </select>
            <label>How many days out of the week can you work?</label><br>
            <input type="number" name="quantity" min="1" max="5">
            <input type="submit" value="Submit" />'''




        page_close = '''
        </form>
    </body>
</html>'''


        if self.request.GET:
            first = self.request.GET['first']
            last = self.request.GET['last']
            email = self.request.GET['email']
            radio = self.request.GET['gender']
            check = self.request.GET['experience']
            select = self.request.GET['education']
            number = self.request.GET['quantity']
            self.response.write(page_head + first + ' ' + last + ' ' + email + ' ' + radio + ' ' + check + ' ' + select + ' ' + number + ' ' + page_close)
        else:
            self.response.write(page_head + page_body + page_close)





















# Dont touch this.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
