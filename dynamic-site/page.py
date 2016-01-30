# this is where the html will be placed
# the inheritance will take place here
# polymorphism will take place here

class Page(object):
    def __init__(self):
        self.title = 'Welcome!'
        self.css = "css/style.css"
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''


        self._body = ''

        self._close = '''
    </body>
</html>'''

    def print_now(self):
        all = self._head + self._body + self._close
        all = all.format(**locals())
        return all


class LinkPage(Page):
    def __init__(self):
        super(LinkPage, self).__init__()

        self.link1 = '<a href="?user=carl">Carl</a>'
        self.link2 = '<a href="?user=roy">Roy</a>'
        self.link3 = '<a href="?user=ned">Ned</a>'
        self.link4 = '<a href="?user=pete">Pete</a>'
        self.link5 = '<a href="?user=heather">Heather</a>'


    def print_now(self):
        return self._head + self._body + self.link1 + self.link2 + self.link3 + self.link4 + self.link5 + self._close












