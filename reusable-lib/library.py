# this will hold the classes that will interpret and calculate the data
# needs to be fully encapsulated
# three utility functions


class PayStub(object):
    def __init__(self):  # initializing function

        self.__check = []  # putting all of the worker's numbers and name into an array

    def add_check(self, c):  # this adds to the check array above
        self.__check.append(c)  # by appending c

    def compile_list(self):  # this compiles the list of items for the check array
        output = ''
        for check in self.__check:  # loops through the items
            output +=  check.name + str(check.hours) + str(check.pay) + str(check.over) + ' <br />'
        return output

    def calc_check(self): # this is a check calculator for how much the employee is due per hours worked and wage per hour
        time = []  # this puts it both the hours worked and the amount per hour in an array
        for check in self.__check:  # loops through the __check array to append the new pay per hour amount
            time.append(check.pay)  # appends it to the time array

        for check in self.__check: # loops through the __check array to append the new hours worked amount
            time.append(check.hours)  # appends it to the time array

        span = int(time[0]) * int(time[1])   # this calculates the number in the first position of the array with the second

        return str(span)  # this returns the check total back to the main

    def over_time(self):  # this calculates overtime based on hours worked
        over = []  # array to hold the overtime hours
        for check in self.__check:  # loops through the __check array to append the new overtime amount
            over.append(check.over)  # this appends the number to the over array

        num = int(over[0]) * 100   # this calculates the overtime hours times by 100

        return str(num)  # returns that number as a string to be printed to window


class JobData(object):   # this is a data object to hold the items from the form
    def __init__(self):

        self.name = ''  # these are temp holding spots for the items to be entered
        self.hours = 0
        self.__pay = 0
        self.over = 0

        @property   # the pay is private so I set upa getter and a setter
        def pay(self):   # method for retrieving the private pay amount above
            return self.__pay

        @pay.setter    # this is the setter for changing the amount paid per hour
        def pay(self, p):
            # checking if info is correct
            if p > 43:   # we do not pay our employees over 43 dollars an hour
                print "Invalid Hourly Rate"   # prints to console
            else:
                self.__pay = p     # returned as p