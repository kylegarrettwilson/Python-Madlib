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
<html
    <head>
    <title></title>



    <style>

    </style>


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
























# Dont touch this.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
