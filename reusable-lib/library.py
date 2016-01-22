# this will hold the classes that will interpret and calculate the data
# needs to be fully encapsulated
# three utility functions





















class JobData(object):
    def __init__(self):

        self.name = ''
        self.hours = 0
        self.__pay = 0
        self.over = 0


        @property
        def pay(self):
            return self.__pay

        @pay.setter
        def pay(self, p):
            # checking if info is correct
            if p > 43:
                print "Invalid Hourly Rate"
            else:
                self.__pay = p