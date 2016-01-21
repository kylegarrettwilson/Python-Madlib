class Page(object):
    def __init__(self):
        self.__title = "Sign Up!"
        self.__css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>

        """

        self.__body = "Welcome to the danger zone"
        self.close = """
    </body>
</html>

        """


        self.whole_page = ""

    def update(self):
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals())


    # GETTERS and SETTERS


    @property
    def body(self):
        return self.__body


    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()




    # write only
    @property   # getter not doing anything, used for a setter
    def title(self):
        return self.__title


    @title.setter
    def title(self, new_title):
        self.__title = new_title
        self.update()





    # write only
    @property
    def css(self):
        return self.__css



    @css.setter
    def css(self, new_css_file):
        self.__css = new_css_file
        self.update()