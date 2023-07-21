my_car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021,
  "interest": 22,
  "makes": ["r", "g",]
}

person_bob = {
    "first_name": "Robert",
    "last_name": "Smith",
    "Nickname": "Bob",
    "age": 42,
    "DOB": "1/2/80"
}
# print(my_car['makes'][0])

# print(len(my_car))

a_car = my_car["model"]

# print(a_car)

key_list = my_car.keys()
val_list = my_car.values()
item_list = my_car.items()

# print(key_list)
# print(val_list)
# print(item_list)

x = my_car.keys()
y = my_car.values()

# print(x)
# print(y)

my_car["con"] = 'fair'
my_car["year"] = 2018

# print(x)
# print(y)

if "model" in my_car:
    print( "ya")

# my_car['brand'] = "Bob"
# my_car['model'] = "silvy"

# print(my_car)

# my_car['color'] = "blue"
# print(my_car)

# my_car.update({"year": 3000})
# my_car.update({"years": 3000})
# print(my_car)

# person_bob.pop('last_name')
# print(person_bob)

# person_bob.popitem()
# print(person_bob)

for key in person_bob:
    if person_bob[key] == str:

        print(key.upper(), person_bob[key].upper())
    # print("values", person_bob[key])

for key, value in person_bob.items():
    print(key, value)