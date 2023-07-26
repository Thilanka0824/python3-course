# ITP Week 3 Day 1 Exercise

# ENUMERATE!

# 1. Read all instructions first!
#
# Prompt: given a list of names, create a list of dictionaries with the index as the user_id and name

users_list = ["Alex", "Bob", "Charlie", "Dexter", "Edgar", "Frank", "Gary"]

# example output

# [{"user_id": 0, "name": "Alex"}, etc, etc]
for str in users_list:
    print({"user_id": users_list.index(str), "name": str})
# print(str)
# print the index of the list
print(users_list.index(str))
# "name": users_list


# 1a. Create a function that takes a single string value and returns the desired dictionary

def str_to_dict(str):
    users_dict_list = []
   
    for str in users_list:
        users_dict_list.append(str)
    
    return users_dict_list

print(str_to_dict(users_list))
    


# 1b. Create a new empty list called users_dict_list

# 1c. Loop through users_list that calls the function for each item and appends the return value to users_dict_list

# 2. Prompt: Given a series of dictionaries and desired output (mock_data.py), can you provide the correct commands?
from mock_data import mock_data

# 2a. retrieve the gender of Morty Smith
print(mock_data['results'][1]['gender'])


# 2b. retrieve the length of the Rick Sanchez episodes
print(len(mock_data['results'][0]['episode']))

# 2c. retrieve the url of Summer Smith location

print(mock_data['results'][2]['location']['url'])

    
