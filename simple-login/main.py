'''
Kyle Wilson
1-14-16
DPW
Simple Login Form
'''


# This is a job application for Mid Oregon Personnel, a staffing agency in Prineville, Oregon.




import webapp2    # This is the web app browser that app engine uses.


class MainHandler(webapp2.RequestHandler):
    def get(self):  # this is like the constructor function for this project, the self below references this.

                    # this is the page head that will take over the html head and css

        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
    <title>Sign Up!</title>



    <style>

    body{
        width: 100%;
        text-align: center;
        background-color: #99e5ff;
    }

    form{
        width: 300px;
        margin: 0 auto;
        text-align: center;
        padding: 20px;
        border: 3px solid black;
        background-color: #d9d9d9

    }


    </style>



    </head>
    <body>'''



        # this is the page body that will contain the form and other html documents

        page_body = '''
            <h1>Welcome to Mid Oregon Personnel</h1>
            <h3>Please fill out our job application!</h3>


            <form method="GET">
            <label>First Name: </label><input type="text" name="first" /><br><br>


            <label>Last Name: </label><input type="text" name="last" /><br><br>


            <label>Email: </label><input type="email" name="email" /><br><br>


            <label>What is the gender that you identify with?</label><br>
            <input type="radio" name="gender" value="male" checked>Male
            <br>
            <input type="radio" name="gender" value="female">Female
            <br>


            <br>
            <input type="radio" name="experience" value="yes" checked>I have a currently have a job
            <br>
            <input type="radio" name="experience" value="no">I do not currently have a job
            <br>

            <br>
            <label>Select the level of education that you have achieved: </label><br>
            <select name="education">
                <option value="doctoral">I have a Phd</option>
                <option value="masters">I have a Masters degree</option>
                <option value="bachelors">I have a Bachelors degree</option>
                <option value="associates">I have an Associates degree</option>
                <option value="nodegree">I do not have a college degree</option>
            </select><br>

            <br>
            <label>How many days out of the week can you work?</label><br>
            <input type="number" name="quantity" min="1" max="5">

            <br>
            <br>
            <input type="submit" value="Submit" />'''


            # this is the page close that contains the html document closures.

        page_close = '''
        </form>
    </body>
</html>'''


        if self.request.GET:  # if you can get these items then print this material
            first = self.request.GET['first']  # this is storing form info in a variable and then using that info for printing
            last = self.request.GET['last']   # this is storing form info in a variable and then using that info for printing
            email = self.request.GET['email']   # this is storing form info in a variable and then using that info for printing
            radio = self.request.GET['gender']   # this is storing form info in a variable and then using that info for printing
            check = self.request.GET['experience']   # this is storing form info in a variable and then using that info for printing
            select = self.request.GET['education']   # this is storing form info in a variable and then using that info for printing
            number = self.request.GET['quantity']   # this is storing form info in a variable and then using that info for printing
            self.response.write(page_head + first + ' ' + last + ' ' + email + ' ' + radio + ' ' + check + ' ' + select + ' ' + number + ' ' + page_close) # this compiles all of the variable info from the form and prints it to the browser.
        else:
            self.response.write(page_head + page_body + page_close)  # this is what will print if the above statements are false. This just happens to be the html doc above so it can be filled out by user.





















# Dont touch this.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
