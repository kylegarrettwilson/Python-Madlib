# Waterman Accounting
# Employee Directory
# each instance is employee name



class Employee(object):    # this is employee function that will work with the main handler on each employees data
    def __init__(self):
        self.name = ""
        self.title = ""
        self.image = ""
        self.bio = ""
        self.email = ""
        self.phone = ""
        self.wage = 0

    def calc_wage(self):  # we needed to have on calculation in our project and I thought price per appointment would be good to know
        total = self.wage * 4   # price per hour times by four hours for average meeting time
        return str(total)  # return total


class Data(object):
    def __init__(self):

        carl = Employee()   # invoking employee class
        carl.name = "Carl Filtz"  # these are all values for the employee attributes above for each specific employee
        carl.title = "Senior Accountant"
        carl.image = "images/carl.jpg"
        carl.bio = "Carl has been the lead accountant for 10 years."
        carl.email = "carl@waterman.com"
        carl.phone = "541-990-8987"
        carl.wage = 70

        roy = Employee() # invoking employee class
        roy.name = "Roy Barnes" # these are all values for the employee attributes above for each specific employee
        roy.title = "Junior Accountant"
        roy.image = "images/roy.jpg"
        roy.bio = "Roy has been a junior accountant for 2 years."
        roy.email = "roy@waterman.com"
        roy.phone = "541-930-7773"
        roy.wage = 34

        ned = Employee() # invoking employee class
        ned.name = "Ned Lighthouse" # these are all values for the employee attributes above for each specific employee
        ned.title = "Junior Accountant"
        ned.image = "images/ned.jpg"
        ned.bio = "Ned has been a junior accountant for 4 years."
        ned.email = "ned@waterman.com"
        ned.phone = "541-960-9292"
        ned.wage = 40

        pete = Employee()  # invoking employee class
        pete.name = "Pete Kohlman" # these are all values for the employee attributes above for each specific employee
        pete.title = "Junior Accountant"
        pete.image = "images/pete.jpg"
        pete.bio = "Pete has been a junior accountant for 3 years."
        pete.email = "carl@waterman.com"
        pete.phone = "541-990-8987"
        pete.wage = 38

        heather = Employee()  # invoking employee class
        heather.name = "Heather Jones" # these are all values for the employee attributes above for each specific employee
        heather.title = "Tax Lawyer"
        heather.image = "images/heather.jpg"
        heather.bio = "Heather is an attorney who specializes in tax law."
        heather.email = "heather@waterman.com"
        heather.phone = "541-340-9983"
        heather.wage = 230

        self.people = [carl, roy, ned, pete, heather]  #placing the data above into an array to access later

