class Page(object):
    def __init__(self):
        self.title = "Sign Up!"
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

        self.body = """
            <h1>Welcome to Mid Oregon Personnel</h1>
            <h3>Please fill out our job application!</h3>


            <form method="GET">
            <label>First Name: </label><input type="text" name="first" /><br><br>


            <label>Last Name: </label><input type="text" name="last" /><br><br>


            <label>Email: </label><input type="email" name="email" /><br><br>


            <label>What is the gender that you identify with?</label><br>
            <input type="radio" name="gender" value="male" checked>Male
            <br>
            <input type="radio" name="gender" value="female">Female
            <br>


            <br>
            <input type="radio" name="experience" value="yes" checked>I have a currently have a job
            <br>
            <input type="radio" name="experience" value="no">I do not currently have a job
            <br>

            <br>
            <label>Select the level of education that you have achieved: </label><br>
            <select name="education">
                <option value="doctoral">I have a Phd</option>
                <option value="masters">I have a Masters degree</option>
                <option value="bachelors">I have a Bachelors degree</option>
                <option value="associates">I have an Associates degree</option>
                <option value="nodegree">I do not have a college degree</option>
            </select><br>

            <br>
            <label>How many days out of the week can you work?</label><br>
            <input type="number" name="quantity" min="1" max="5">

            <br>
            <br>
            <input type="submit" value="Submit" />
            </form>"""

        self.close = """
    </body>
</html>

        """


    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all


