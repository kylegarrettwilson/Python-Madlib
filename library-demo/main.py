
import webapp2
from library import MovieData, FavoriteMovies
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # page for class
        p = Page()
        lib = FavoriteMovies()







        #use form to get this info
        #movie title
        #movie year
        #director

        md1 = MovieData()
        md1.title = "Star Wars"
        md1.year = 1989
        md1.director = "George Lucas"
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "Forrest Gump"
        md2.year = 1999
        md2.director = "Pedro Lopez"
        lib.add_movie(md2)




        lib.calc_time_span()
        p.body = lib.compile_list() + lib.calc_time_span()
        self.response.write(p.print_out())
















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
