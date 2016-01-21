# need a data object
class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []

        # to do: have an array to hold movie info
        # some way to add to that array
        # generate a list at the end
        # calculate time span



        # adding the movies one at a time
    def add_movie (self, m):
        self.__movie_list.append(m)




    def compile_list(self):
        output = ''
        for movie in self.__movie_list:
            output += 'Title: ' + movie.title + str(movie.year) + movie.director + ' <br />'
        return output





    def calc_time_span(self):
        # calculate time in between movies
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)

            # sort them
        years.sort()


        num = len(years) - 1
        span = years[num] - years [0]

        return str(span)






class MovieData(object):
    def __init__(self):
        self.title = ''
        self.__year = 0  # check for a valid year
        self.director = ''



        # this is a setter, changing self.__year
        @property
        def year(self):
            return self.__year

        @year.setter
        def year(self, y):
            # checking if info is correct
            if y > 2016:
                print "Invalid date"
            else:
                self.__year = y
