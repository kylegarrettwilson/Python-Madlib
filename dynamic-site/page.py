# this is where the html will be placed
# the inheritance will take place here
# polymorphism will take place here

class Page(object):
    def __init__(self):
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

    def print_now(self):
        all = self._head + self.body + self._close
        return all


class LinkPage(Page):
    def __init__(self):
        super(LinkPage, self).__init__()

        self.link1 = '<a href="?user=carl">Carl</a>' + ' '
        self.link2 = '<a href="?user=roy">Roy</a>' + ' '
        self.link3 = '<a href="?user=ned">Ned</a>' + ' '
        self.link4 = '<a href="?user=pete">Pete</a>' + ' '
        self.link5 = '<a href="?user=heather">Heather</a>' + ' '

        self.total_link = '<nav>' + self.link1 + self.link2 + self.link3 + self.link4 + self.link5 + '</nav>'

        self.section_open = '<section>'
        self.section_filler = '<p>Pick one of our dedicated professionals</p>'
        self.inputs = ''
        self.section_close = '</section>'

    def print_now1(self):
        return self._head + self.body + self.total_link + self.section_open + self.section_filler + self.section_close + self._close

    def print_now2(self):
        return self._head + self.body + self.total_link + self.section_open + self.inputs + self.section_close + self._close












