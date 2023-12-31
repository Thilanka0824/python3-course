# ITP Week 2 Day 4 Exercise
import random
# 1. Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 0
}

# SCENARIO: A person came in and bought one of everything!

# for item in inventory:
    # decrement item by using an assignment operator
for item in inventory:
    if inventory[item] > 0:
        inventory[item] -= 1 

    # NOTE: recall that item represents the key of the key:value pair

# print(inventory)
# 2. Implicit Functions 
# (When we work with global variables/objects and don't return anything, 
# these functions are implicit return functions!)

    # a. Dictionaries - create a function that takes in a dictionary which updates the "role" key value pair and makes it uppercase

user_1 = {
    "firstName": "Stephanie",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "95485"
}

user_2 = {
    "firstName": "Brion",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "67344"
}

user_3 = {
    "firstName": "Daniel",
    "lastName": "Kim",
    "role": "Instructor", 
    "id": "74324"
}

user_4 = {
    "firstName": "Thilanka",
    "lastName": "Rodrigo",
    "role": "Student", 
    "id": "08244"
}

def update_role(user):
    for key, value in user.items(): #
        if key == "role":
            key_name = key.upper()
            # print(key_name)
            user[key] = user[key].upper() 
            
            
    return user
            

        

            

    # b. Dictionaries - Run the functions (3 times for each user!)

instructor_list = [user_1, user_2, user_3, user_4]
update_role(instructor_list[0])
update_role(instructor_list[1])
update_role(instructor_list[2])
update_role(instructor_list[3])
# print(instructor_list)


    # c. List - create a function that takes in the list and 

def is_instructor(list):
  
    for dictionary in list: #for the list of objs
        if "id" in dictionary: 
            new_id = str(random.randint(10000, 99999))
            dictionary["id"] = new_id
            # print(dictionary)

        if dictionary.get("role") == "INSTRUCTOR":
            print("VALID", dictionary)
        else:
            print("INVALID", dictionary)
    
    
            
    # checks if the each user's role is equal to "INSTRUCTOR". 
    # if it is the same, print VALID else print INVALID (try to use a loop here!)
is_instructor(instructor_list)
# role_check(instructor_list)

    # d. import the random module and update the function to re-assign the id of each user

    # e. don't forget to run it!
    
# 3. Explicit Functions
user_info = [46453, "Devin", "Smith", 78659, "Harley", "Quinn",]
    # Each element by index of user_info follows the format of: id, first_name, last_name

    # Create a function with a parameter user_list
    #   - return a dictionary with the follow key value pairs:
    #   - id: user_list[0]
    #   - first_name: user_list[1]
    #   - last_name: user_list[2]

# def dictionary_creator(user_info_list):
#     for i in user_info_list:
#         return {
#             "id": user_info_list[0],
#             "first_name": user_info_list[1],
#             "last_name": user_info_list[2],
#         }

def dictionary_creator(user_info_list):
    users = []
    if len(user_info_list) % 3 == 0:
        for i in range(0, len(user_info_list), 3):
            user_dict = {
                "id": user_info_list[i],
                "first_name": user_info_list[i + 1],
                "last_name": user_info_list[i + 2],
            }
            users.append(user_dict)
    else:
        return print("list must be divisible by 3")
    return users



print(dictionary_creator(user_info))