# ITP Week 1 Day 4 Exercise

# EASY

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1. loop through the lowercase and print each element
for element in lowercase:
    print(element)

# 2. loop through the lowercase and print the capitalization of each element
for element in lowercase:
    print(element.upper())

# MEDIUM

# 1. create a new variable called uppercase with an empty list
uppercase = []

# 2. loop through the lowercase list
    # 2a. append the capitalization of each element to the uppercase list
for element in lowercase:
    uppercase.append(element.upper())

# HARD

# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.

password = input(
    "Enter a password with a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character: ")

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# 1. create the following variables and assign them Booleans as False
    # has_uppercase 
    # has_lowercase
    # has_number
    # has_special_char

has_uppercase = False
has_lowercase = False
has_number = False
has_special_char = False



# 2. loop through the string password (same as a list)
# OR you can create a new list variable of the string password
# using list(string) NOTE: assign it a new variable as such:
# password_list = list(password) prior to looping.
# for element in password:
#     if element in uppercase:
#         has_uppercase = True
#     elif element in lowercase:
#         has_lowercase = True
#     elif element in special_char:
#         has_special_char = True
#     elif element in range(11):
#         has_number = True

# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.
for element in password:
        if element in uppercase:
            has_uppercase = True
        elif element in lowercase:
            has_lowercase = True
        elif element in special_char:
            has_special_char = True
        elif element.isdigit(): # I found this on stack overflow and it works!
            has_number = True




# NOTE: to see if it has a number, use range from 0 - 10!

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)
# nightmare = [has_uppercase, has_lowercase, has_special_char, has_number]
nightmareReasons = ["No uppercase", "No lowercase",
                    "No special character", "No number"]




if has_uppercase and has_lowercase and has_special_char and has_number:
     print("SAFE STRONG PASSWORD")
else:
    print("Update password: too weak")

if (has_uppercase == False):
    print(nightmareReasons[0])
if (has_lowercase == False):
    print(nightmareReasons[1])
if (has_special_char == False):
    print(nightmareReasons[2])
if (has_number == False):
    print(nightmareReasons[3])


# final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True

# NOTE: we can shorthand this by just checking if the variable exists (returns True)
#final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
# this will fail the same if any one of them is False

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop


# BONUS: update the password variable to take in an user input!

# NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!

# nightmare = [has_uppercase, has_lowercase, has_special_char, has_number]
# nightmareReasons = ["No uppercase", "No lowercase",
#                     "No special character", "No number"]

# for reason in nightmare:  
#     if reason == False:
#         print(nightmareReasons[reason])

#this doesnt work. I think i need a nested loop for it to work but im not sure of how to do it in python