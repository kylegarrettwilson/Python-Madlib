# store user inputs and then encapsulate
# calc check total
# calc overtime total
# calc total hours worked each week on average
# calc some type of bonus




class JobData(object):   # this is a data object to hold the items from the form
    def __init__(self):   # initializing function

        self.__name = ''  # these are temp holding spots for the items to be entered
        self.__hours = 0  # these are temp holding spots for the items to be entered
        self.__pay = 0   # these are temp holding spots for the items to be entered
        self.__over = 0   # these are temp holding spots for the items to be entered

        @property    # This is a getter for the private attribute above self.__name
        def name(self):    #This is the function which can be accessed by name for the setter
            return self.__name   # this is returning the private attribute above so it can be changed using the setter

        @name.setter  # This is the setter for the getter titled name
        def name(self, n):   # This is the function for the setter which passes in "n" and uses that value to set the new value for self.__name
            self.__name = n   # This is updating the private function above with the new "n" value

        @property   # This is a getter for the private attribute above self.__over
        def over(self):   #This is the function which can be accessed by over for the setter
            return self.__over  # this is returning the private attribute above so it can be changed using the setter

        @over.setter    # this is the setter for the getter titled over
        def over(self, o):  # this is a function that passes in "o" as a way of updating the self.__over
            if o > 60:   # this setter is actually doing more then just setting it to a new value, it is calculating an if else statement
                print "You need to talk to an adviser"   # if o is greater than 60 then print this
            else:  # if o is not greater then 60
                self.__over = o   # the private attribute above is replaced with the value of "o"

        @property   # I want the hours to be private so it can't be easily messed with, this is a getter
        def hours(self):  # this is what the new reference name will be for the private hours above
            return self.__hours   # returning the private attribute above so the setter can update it

        @hours.setter   # this is the setter for the hours worked for private attribute self.__hours
        def hours(self, h):  # method for updating using a passed in value for "h"

            if h > 40:  # cannot work more than 40 hours a week, it would be overtime for extra
                print "Any overtime needs be calculated in the overtime field"  # change input fields
            else: # if h is not greater than 40
                self.__hours = h   # the new hours setter is updating the private attribute

        @property   # the pay is private so I set upa getter and a setter
        def pay(self):   # method for retrieving the private pay amount above
            return self.__pay  # return the private attribute so it can be updated using setter

        @pay.setter    # this is the setter for changing the amount paid per hour
        def pay(self, p):   # passing in "p" as a way of updating the value for self.__pay above
            # checking if info is correct
            if p > 43:   # we do not pay our employees over 43 dollars an hour
                print "Invalid Hourly Rate"   # prints to console
            else:  # if p is not greater than 43
                self.__pay = p     # returned as p

    def calc_check(self):  # this is a function that calcs the check total depending on pay per hour and hours worked

        total = int(self.hours) * int(self.pay)   # this is hours worked times by pay for a check total

        return str(total)   # total returned for the check amount

    def over_time(self):   # this is a funciton that calcs the overtime pay

        num = int(self.over) * (int(self.pay * 2))   # overtime is charged as double pay

        return str(num)  # return num for overtime amount

    def total_time(self):  # this is the average amount of hours worked per week

        time = (int(self.hours) + int(self.over)) / 4   # hours plus overtime divided by four weeks in a month

        return str(time)  # return total time

    def bonus(self):   # bonus calculator
        if int(self.over) > 35:   # if you work greater than 35 overtime hours then you get a bonus
            return str('You have qualified for a bonus!')   # return this string to let them know
        else:
            return str('Keep up the good job!')   # return this if lower then 35






















