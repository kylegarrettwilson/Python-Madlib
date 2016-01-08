# Name: Kyle Wilson
# Class: DPW 2016
# Date: 1-7-16

'''
Hello and welcome to my rental car madlib!

Here are the steps that I followed to complete this assignment:



'''


customer_name = raw_input("Enter your name:  ")

car_type = raw_input("Enter the vehicle you wish to drive:  ")

car_color = raw_input("Do you want a white or red vehicle:  ")

passenger_count = raw_input("Enter the number of passengers (including yourself):  ")

miles_count = raw_input("Enter the number of miles you will drive:  ")

years_driving = raw_input("Enter the number of years you have had a license:  ")


print "Hello and welcome " + customer_name + ". Thank you for choosing Rad Rentals."


# one array

cars = ["Cobalt", "Nova", "Mustang", "Panel Van"]
cars.append(car_type)
print "The vehicles we have availabe are ", cars



# one dictionary

color = dict()
color = {"white":"granny", "red":"speed freak"}
print "The color you chose says a lot about who you are. You must be a", color[car_color]




# two conditionals

if passenger_count <= 5:
    setup = "any"
    print "You can select " + setup + " car you want."
else:
    print "You have too many passengers, lose some or get the van."



if miles_count > 100:
    conserve = "Eco Friendly"
    print "You are traveling too many miles for a gas guzzler. Take the " + conserve + " Alternative."
else:
    print "You aren't going far, take the sports car."



# one function

def gasMilage(x, y):
    gas = x / y
    return gas

a = gasMilage(miles_count, 22)
print "You use roughly " + str(a) + " gallons of gas."



# one loop

if years_driving <= 10:
    i = years_driving
for i in range(0, 10):
    print "You have been driving for " + str(i) + " years. "
else:
    print "You have been driving for too many years to count."


























