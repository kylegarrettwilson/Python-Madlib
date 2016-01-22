# this will hold the classes that will interpret and calculate the data
# needs to be fully encapsulated
# three utility functions


class PayStub(object):
    def __init__(self):

        self.__check = []

        # to do: have an array to hold movie info
        # some way to add to that array
        # generate a list at the end
        # calculate time span

    def add_check(self, c):
        self.__check.append(c)

    def compile_list(self):
        output = ''
        for check in self.__check:
            output +=  check.name + str(check.hours) + str(check.pay) + str(check.over) + ' <br />'
        return output

    def calc_check(self):
        time = []
        for check in self.__check:
            time.append(check.pay)

        for check in self.__check:
            time.append(check.hours)

        span = int(time[0]) * int(time[1])

        return str(span)


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