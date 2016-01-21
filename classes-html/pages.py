class Page(object):
    def __init__(self):
        self.__title = "Sign Up!"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>

        """

        self.body = "Welcome to the danger zone"
        self.close = """
    </body>
</html>

        """


    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all
