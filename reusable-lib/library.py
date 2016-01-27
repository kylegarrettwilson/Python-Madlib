# store user inputs and then encapsulate
# calc check total
# calc overtime total
# calc total hours worked each week on average
# calc some type of bonus




class JobData(object):   # this is a data object to hold the items from the form
    def __init__(self):

        self.name = ''  # these are temp holding spots for the items to be entered
        self.__hours = 0  # these are temp holding spots for the items to be entered
        self.__pay = 0   # these are temp holding spots for the items to be entered
        self.over = 0   # these are temp holding spots for the items to be entered


        @property   # I want the hours to be private so it can't be easily messed with, this is a getter
        def hours(self):  # this is what the new reference name will be for the private hours above
            return self.__hours

        @hours.setter   # this is the setter for the hours worked
        def hours(self, h):  # method for updating

            if h > 40:  # cannot work more than 40 hours a week, it would be overtime for extra
                print "Any overtime needs be calculated in the overtime field"  # change input fields
            else:
                self.__hours = h   # the new hours setter

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

    def calc_check(self):  # this calcs the check total depending on pay per hour and hours worked

        total = int(self.hours) * int(self.pay)   # this hours worked times by pay

        return str(total)   # total returned

    def over_time(self):   # this calcs the overtime pay

        num = int(self.over) * (int(self.pay * 2))   # overtime is charged as double pay

        return str(num)  # return num

    def total_time(self):  # this is the average amount of hours worked per week

        time = (int(self.hours) + int(self.over)) / 4   # hours plus overtime divided by four weeks in a month

        return str(time)  # return time

    def bonus(self):   # bonus calculator
        if int(self.over) > 35:   # if you work greater than 35 overtime hours then you get a bonus
            return str('You have qualified for a bonus!')   # return this string to let them know
        else:
            return str('Keep up the good job!')   # return this if lower then 35






















