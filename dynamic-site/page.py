# this is where the html will be placed
# the inheritance will take place here
# polymorphism will take place here

class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = ''
        self._close = '''
    </body>
</html>'''

    def print_now(self):
        return self._head + self._body + self._close
            