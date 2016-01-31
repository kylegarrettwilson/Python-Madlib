# this is where the html will be placed
# the inheritance will take place here
# polymorphism will take place here

class Page(object): # this is a super class, used as a template
    def __init__(self): # initializing function
        self.css = "css/style.css"
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Welcome!</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
        <link href='https://fonts.googleapis.com/css?family=Roboto:500,700,900,300,100,400' rel='stylesheet' type='text/css'>
    </head>
    <body>'''

        self.body = '''
        <h1>Waterman Accounting</h1>
        <h3>"We protect you from the IRS!"</h3>

                    '''

        self.section_open = ''

        self._close = '''
    </body>
</html>'''

    def print_now(self): # this is one example of polymorphism below, I have to examples on this page
        all = self._head + self.body + self._close  # this collects all attributes above
        return all  # returns all of them


class LinkPage(Page):   # this is a sub class
    def __init__(self):  # initializing function
        super(LinkPage, self).__init__()    # this is the constructor function for the super class

        self.link1 = '<a href="?user=carl">Carl</a>' + ' '   # this is the html for link 1
        self.link2 = '<a href="?user=roy">Roy</a>' + ' '    # this is the html for link 2
        self.link3 = '<a href="?user=ned">Ned</a>' + ' '     # this is the html for link 3
        self.link4 = '<a href="?user=pete">Pete</a>' + ' '    # this is the html for link 4
        self.link5 = '<a href="?user=heather">Heather</a>' + ' '   # this is the html for link 5

        self.total_link = '<nav>' + self.link1 + self.link2 + self.link3 + self.link4 + self.link5 + '</nav>'  # I wanted all of the links to be in a nav tag so I placed all the variables here together

        self.section_open = '<section>'   # this is an example of polymorphism and it begins the html for the entire employee section when user clicks on name
        self.section_filler = '<p>Pick one of our dedicated professionals</p>'   # this is the prompt first given to the user to click a name
        self.inputs = ''   # this is where the input fields are going to go from the main handler class
        self.section_close = '</section>'   # this is the end tag for that polymorphism above

    def print_now1(self):   # this is the first print out if there are now values in the url
        return self._head + self.body + self.total_link + self.section_open + self.section_filler + self.section_close + self._close

    def print_now2(self):  # this is the second print out if there are values in the url
        return self._head + self.body + self.total_link + self.section_open + self.inputs + self.section_close + self._close












