# Waterman Accounting
# Employee Directory
# each instance is employee name


class Employee(object):
    def __init__(self):
        self.name = ""
        self.title = ""
        self.image = ""
        self.bio = ""
        self.email = ""
        self.phone = ""


class Data(object):
    def __init__(self):

        carl = Employee()
        carl.name = "Carl Filtz"
        carl.title = "Senior Accountant"
        carl.image = "carl.jpg"
        carl.bio