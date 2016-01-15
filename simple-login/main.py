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
    '''
























# Dont touch this.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
