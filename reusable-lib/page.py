# this needs to have two classes.
# one class is FormPage, this will take in the data from the user
# second class is ResultsPage and this will display the information after it has been calculated
# the HTML needs to be in view classes
# at least four input from the user


class FormPage(object):  # this is the form page class for holding the html elements
    def __init__(self):  # initializing function
        self.title = "Welcome!"  # this is a variable that changes the self.title in html
        self.__css = "css/styles.css"  # this is a link to the css file from the yaml file
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = """
            <form method="GET">
                <label>Enter your last name: </label><br>
                <input type="text" name="last" /><br><br>

                <label>Enter the number of hours worked this week (must be between 0 and 40): </label><br>
                <input type="number" name="hours" min="0" max="40"><br><br>

                <label>Enter the amount you are paid per hour: </label><br>
                <input type="number" name="pay"><br><br>

                <label>Enter the number of over time hours you worked this week: </label><br>
                <input type="number" name="over" min="0" max="40"><br><br>


                <br>
                <br>
                <input type="submit" value="Submit" />

            </form>

        """

        self.close = """
    </body>
</html>

        """
        # the self.head self.body and self.close hold all of the necessary html elements for the form so they can be printed to the window from the mainhandler class
    def print_out(self):  # this is sending back the html above to the mainhandler class
        all = self.head + self.body + self.close   # combining the html elements all together
        all = all.format(**locals())   # this uses the locals function to change the html title, css and all local attributes
        return all   # return the entire html page with print out

    # write only
    @property  # this is a getter for the private css attribute above
    def css(self):  # this is the function for the getter to be used by the setter
        return self.__css   # returning the private attribute above

    @css.setter  # this is a setter for the css file so we can implement the correct file
    def css(self, css_file):   # this is using a instance attribute to change the css file, it is a function
        self.__css = css_file   # chaning the private attribute value to the new css file


class ResultsPage(object):    # this is the results html page to be printed after the form is submitted by the user
    def __init__(self):   # initializing function
        self.__title = "Welcome"    # this is a title attribute
        self.css = "css/styles2.css"  # this is choosing a different css than the first html page
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your info:</title>
        <link href="css/styles2.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """


        self.body = ""
        self.__error = ''  # not going to use
        self.__close = """
    </body>
</html>
        """
        # this is where the results will print to the window, the self.body is empty because the mainhandler will be putting the info calculated in the library classes to that spot in the html
    def print_out_second(self):   # this is a way of sending back the html to the mainhandler class
        all = self.__head + self.body + self.__error + self.__close   # combining all of the html elements together
        return all  # returning all of the html so it can be displayed by mainhandler if else statement

























