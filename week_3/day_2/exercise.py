# ITP Week 3 Day 2 Exercise

# import in the two modules for making API calls and parsing the data
import json
import requests

# set a url variable to "https://rickandmortyapi.com/api/character"
url = "https://rickandmortyapi.com/api/character"

# set a variable response to the "get" request of the url
response = requests.get(url)

# print to verify we have a status code of 200
print(response)

# assign a variable json_data to the responses' json
json_data = response.json()
json_data = response.text
# print to verify a crazy body of strings!
# print(json_data)

# print(json_data)
posts = json.loads(json_data)

# lets make it into a python dictionary by using the appropriate json method
# rick_and_morty_json = json.loads(json_data)
# rick_and_morty_json = json_data

# print the newly created python object
# print(json_data)

print(posts)