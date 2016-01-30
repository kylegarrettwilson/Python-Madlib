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

        self._body = '<section> '

        self._close = '''
    </body>
</html>'''

    def print_now(self):
        all = self._head + self._body + self._close
        all = all.format(**locals())
        return all


class ContentPage(Page):
    def __init__(self):
        super(Page, self).__init__()

        self.list_open =

    def print_now(self):
        return self._head + self._body + self.link + self._close






    #@property
    #def inputs(self):
      #  pass

    #@inputs.setter
   # def inputs(self, ar):
      #  self.__inputs = ar
      #  for item in ar:
      #      self.__link_inputs += ''











