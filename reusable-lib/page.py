# this needs to have two classes.
# one class is FormPage, this will take in the data from the user
# second class is ResultsPage and this will display the information after it has been calculated
# the HTML needs to be in view classes
# at least four input from the user


class FormPage(object):  # this is the form page class for holding the html elements
    def __init__(self):  # constructor method
        self.title = "Welcome!"  # this is a variable that changes the self.title in html
        self.__css = "css/styles.css"  # this is a link to the css file from the yaml
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
                <label>Enter your last name: </label>
                <input type="text" name="last" /><br><br>

                <label>Enter the number of hours worked this week (must be between 0 and 40): </label><br>
                <input type="number" name="hours" min="0" max="40"><br>

                <label>Enter the amount you are paid per hour: </label><br>
                <input type="number" name="pay"><br>

                <label>Enter the number of over time hours you worked this week: </label><br>
                <input type="number" name="over" min="0" max="40"><br>


                <br>
                <br>
                <input type="submit" value="Submit" />

            </form>

        """

        self.close = """
    </body>
</html>

        """

    def print_out(self):  # this is sending back the html above to the mainhandler class
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

    # write only
    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, css_file):
        self.__css = css_file


class ResultsPage(object):    # this is the results html page to be printed after the form is submitted
    def __init__(self):
        self.__title = "Welcome"
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your info:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """


        self.body = ""
        self.__error = ''  # not going to use
        self.__close = """
    </body>
</html>
        """

    def print_out_second(self):   # this is a way of sending back the html to the mainhandler class
        all = self.__head + self.body + self.__error + self.__close
        return all

























