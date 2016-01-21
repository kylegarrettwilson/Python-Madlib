class Page(object):
    def __init__(self):
        self.__title = "Welcome"
        self.css = "css/style.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your info:</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """


        self.body = ""
        self.__error = ''  # not going to use
        self.__close = """
    </body>
</html>
        """


    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all