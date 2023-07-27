import json

example_dict = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ["Ann", "Billy"],
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1, "a": 5}
    ]
}



json_dict = json.dumps(example_dict)
# print(json_dict)

indented = json.dumps(example_dict, indent=4)

# print(indented)

separated = json.dumps(example_dict, indent=4, separators=(". ", "< "))
# print(separated)

sorted = json.dumps(example_dict, indent=4, sort_keys=True)
print(sorted)