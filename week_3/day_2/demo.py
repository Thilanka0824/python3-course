import json
import requests

from dummy_json import dummy_json

# json.loads(dummy_json)

converted_json_dictionary = json.loads(dummy_json)

# print(converted_json_dictionary)

converted_json_dictionary['researcher']['relatives'][0]['name']

# dumps is the opposite of loads
# converted_json =  json.dumps(converted_json_dictionary, indent=4, sort_keys=True)
# converted_json =  json.dumps({"test":"good"})



url = 'https://jsonplaceholder.typicode.com/posts' # this is the endpoint

response = requests.get(url) # this is the request

# print(response) # returns a Response class
# json_data = response.json() # returns a list of dictionaries <--- normal method of jsonification
json_data = response.text # returns a list of dictionaries #use this if jsonify doesn't work
posts = json.loads(json_data) # returns a list of dictionaries
print(posts)

