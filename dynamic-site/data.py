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
        carl.bio = "Carl has been the lead accountant for 10 years."
        carl.email = "carl@waterman.com"
        carl.phone = "541-990-8987"

        roy = Employee()
        roy.name = "Roy Barnes"
        roy.title = "Junior Accountant"
        roy.image = "roy.jpg"
        roy.bio = "Roy has been a junior accountant for 2 years."
        roy.email = "roy@waterman.com"
        roy.phone = "541-930-7773"

        ned = Employee()
        ned.name = "Ned Lighthouse"
        ned.title = "Junior Accountant"
        ned.image = "ned.jpg"
        ned.bio = "Ned has been a junior accountant for 4 years."
        ned.email = "ned@waterman.com"
        ned.phone = "541-960-9292"

        pete = Employee()
        pete.name = "Pete Kohlman"
        pete.title = "Junior Accountant"
        pete.image = "pete.jpg"
        pete.bio = "Pete has been a junior accountant for 3 years."
        pete.email = "carl@waterman.com"
        pete.phone = "541-990-8987"

        heather = Employee()
        heather.name = "Heather Jones"
        heather.title = "Tax Lawyer"
        heather.image = "heather.jpg"
        heather.bio = "Heather is an attorney who specializes in tax law."
        heather.email = "heather@waterman.com"
        heather.phone = "541-340-9983"

        self.people = [carl, roy, ned, pete, heather]

