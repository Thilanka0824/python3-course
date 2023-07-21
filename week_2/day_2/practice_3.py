# ITP Week 2 Day 2 (In-Class) Practice 3

# Functions Parameters and Arguments

# Lets take those functions we built in practice_2 and make them more dynamic:

# Rewrite the functions from practice_2 using parameters:
# add_num
def add_num(x, y):
    print(int(x) + int(y))

add_num(input("For Adding. Enter a number: "), input("Enter a number: " ))

# subtract_num
def subtract_num(x, y):
    print(int(x) - int(y))

subtract_num(input("For Subtracting. Enter a number: "), input("Enter a number: " ))

# multiply_num
def multiply_num(x, y):
    print(int(x) * int(y))

multiply_num(input("For multiplication. Enter a number: "), input("Enter a number: " ))

# divide_num
def div_num(x, y):
    print(int(x) / int(y))


div_num(input("For Division. Enter a number: "), input("Enter a number: " ))
# div_num(input("Enter a number: "), input("Enter a number: " ))

# Don't forget to call your functions to make sure they work

#Uncomment to call your functions:
# print("I should see the number 7 below from add_num: ")
# add_num(3, 4)

# print("I should see the number -2 below from subtract_num: ")
# subtract_num(6, 8)

# print("I should see the number 18 below from multiply_num: ")
# multiply_num(2, 9)

# print("I should see the number 2 below from divide_num: ")
# divide_num(10, 5)

# Extra Time?

# Now take in 2 users inputs and pass them 
# in as arguments when calling the functions



