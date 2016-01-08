# Name: Kyle Wilson
# Class: DPW 2016
# Date: 1-7-16

'''
Hello and welcome to my rental car madlib!

Here are the steps that I followed to complete this assignment:

I first created the raw input prompts for the user so I was able to collect all the data I would need at the beginning.

Then I decided to print the name of the customer and welcome them

Then I wanted to use the strings first so I started with an array of car types. I also thought this
made sense because it is one of the first things I would want them to pick

Then I used a dictionary to explain the meaning behind the color they picked for their vehicle

Then I set up two conditionals to hand passenger count and miles count. I wanted to make an if else statement that
controlled the amount of passangers they could have as well as the type of vehicle depending on the number of miles to travel

Then I set up a funtion to handle the number of gallons of gas they would use for the suspected travel distance. I did this by taking the
miles count and dividing it by the average MPG for all of the vehicles in stock, which is 22.


Finally I made a while loop that would alert if they have not been driving for more then ten years and therefore need a cosigner or many of them
for security. If they have been driving for more then ten years then it does not alert.



'''


customer_name = raw_input("Enter your name:  ")   # This is accepting a string

car_type = raw_input("Enter the vehicle you wish to drive:  ")  # This is accepting a string

car_color = raw_input("Do you want a white or red vehicle:  ")  # This is accepting a string

passenger_count = raw_input("Enter the number of passengers (including yourself):  ")  # This is accepting a number

miles_count = int(raw_input("Enter the number of miles you will drive:  ")) # This is accepting a number

years_driving = int(raw_input("Enter the number of years you have had a license:  ")) # This is accepting a number


print "Hello and welcome " + customer_name + ". Thank you for choosing Rad Rentals."  # This is printing and welcoming them


# one array

cars = ["Cobalt", "Nova", "Mustang", "Panel Van"]  # this is an array of cars in the cars variable
cars.append(car_type)   # this appends a new car name based on what they entered above
print "The vehicles we have availabe are ", cars  # this prints the array



# one dictionary

color = dict()  # this is a dictionary
color = {"white":"granny.", "red":"speed freak."}  # this is giving each key and their corresponding output, clients color choice and comparing it with the dict
print "The color you chose says a lot about who you are. You must be a", color[car_color]  # this is printing the clients color choice and comparing it with the dict




# two conditionals

if passenger_count <= 5: # this is an if else statement that is using a logical operator  that is working off of the raw inputs
    setup = "any"
    print "You can select " + setup + " car you want." # this is a cool way of injecting a string into the print
else:
    print "You have too many passengers, lose some or get the van." # this prints if the other part is false



if miles_count > 100:  # this is an if else statement that is working off of the raw inputs
    conserve = "Eco Friendly"
    print "You are traveling too many miles for a gas guzzler. Take the " + conserve + " Alternative."  # this is a cool way of injecting a string into the print
else:
    print "You aren't going far, take the sports car."   # this prints if the other part is false



# one function

def gasMilage(x, y):  # this is a function that is taking in two parameters
    gas = x / y   # miles to travel divided by 22
    return gas  # return solution

a = gasMilage(miles_count, 22)  # this is invoking the function with the raw input and 22
print "You will use roughly " + str(a) + " gallons of gas."  # this prints out the answer to the math above



# one loop


i = years_driving  # this is a while loop that is making i the raw input from above
while i < 10:  # while years driving is under 10
    print "You need a cosigner. You need at least " + str(i) + " responsible adults in the car. "  # print you need how many cosigners based on loop
    i = i+1  # add one to i to keep it incrementing.



























