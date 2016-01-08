print "Hello World"


# one line comments

'''
this is multiple lines (doc strings)

'''




first_name = "Kermit"
last_name = "The Frog"

response = raw_input("Enter your name ")

print "Hello there, ", response




#expressions

birth_year = 1989
current_year = 2016
age = current_year - birth_year
print "You are " + str(age) + " years old"

# int(var)










#conditions



budget = 200


if budget > 100:
    brand = "nike"
    print "yay! by the " + brand
else:
    print "save your money"


budget = 80


if budget > 100:
    brand = "nike"
    print "yay! by the " + brand
elif budget > 70:
    print "buy some knock offs"
else:
    print "save your money"
    # can also do pass to continue












# array

characters = ["mark", "ted", "ned"]
characters.append("kyle")
print characters[0]


movie = dict() #creates this dictionary

movies = {"star wars":"darth vader", "star trek":"ted"}

# key first

print movies["star wars"]  # this will print darth vader











#loops (while and for)

#while not used as often



#will loop any number of times

i = 0
while i<9:
    print "the count is", i
    i = i+1


# will loop a specific amount of times

for i in range(0,10):
    print "the count is", i
    i = i+1



# great for going through arrays

rappers = ["MGK", "Biggie", "tupac"]
for r in rappers:
    print "Here is a rapper"














# functions  def = definitions

def calcArea(h, w):
    area = h * w
    return area


#call it (invoke)

a = calcArea(20, 40)

print str(a) + "sqft"








weight = 200
height = 45
message = '''
Your height is {height} and your weight is {weight}
'''

message = message.format(**locals())

print message

























































