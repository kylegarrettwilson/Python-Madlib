# this needs to have two classes.
# one class is FormPage, this will take in the data from the user
# second class is ResultsPage and this will display the information after it has been calculated
# the HTML needs to be in view classes
# at least four input from the user


class FormPage(object):  # this is the page class for holding the html elements
    def __init__(self):  # constructor method
        self.title = "Welcome!"  # this is a variable that changes the self.title in html
        self.css = "css/style.css"  # this is a link to the css file from the yaml
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>