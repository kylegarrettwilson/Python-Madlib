'''
Kyle Wilson
1-14-16
DPW
Simple Login Form
'''







import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html
    <head>
    <title></title>



    <style>

    </style>


    </head>
    <body>'''





    page_body = '''<form method="GET">
        <label></label><input type="text" name="" />
        <label></label><input type="text" name="" />
        <label></label><input type="text" name="" />
        <input type="radio" name="" value="" checked>...
        <input type="radio" name="" value="" checked>...
        <select name="">
            <option value="">...</option>
            <option value="">...</option>
            <option value="">...</option>
            <option value="">...</option>
        </select>
        <input type="submit" value="Submit" />'''




    page_close = '''
        </form>
    </body>
</html>'''
























# Dont touch this.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
