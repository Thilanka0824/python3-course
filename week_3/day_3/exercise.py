# ITP Week 3 Day 3 Exercise

# RICK AND MORTY API DOCS: https://rickandmortyapi.com/documentation

# we want to make a copy of the Rick and Morty database (which is provided through the api)

character_url = "https://rickandmortyapi.com/api/character"

# EASY MODE

# import the appropriate modules (you have 3)

# set up a workbook and worksheet titled "Rick and Morty Characters"

# assign a variable 'data' with the returned GET request

# create the appropriate headers in openpyxl for all of the keys for a single character

# loop through all of the 'results' of the data to populate the rows and columns for each character

# NOTE: due to the headers, the rows need to be offset by one!

# MEDIUM MODE

# create 2 new worksheets for "Rick and Morty Locations" and "Rick and Morty Episodes"

# create 2 new variables for character_url and location_url (retrieve it from the docs!)

# populate the new worksheets appropriately with all of the data!

# NOTE: don't forget your headers!

# HARD MODE

# Can you decipher the INFO key of the data to use "next" url to continuously pull data?
# Currently, we are only pulling 20 items per api pull!
# WE WANT EVERYTHING. (contact instructors for office hours if stuck!)

# NIGHTMARE

# The inner information for characters, locations, and episodes, references one another through urls
# ie. for episode 28, it lists all the character but by their url

"""
{
  "id": 28,
  "name": "The Ricklantis Mixup",
  "air_date": "September 10, 2017",
  "episode": "S03E07",
  "characters": [
    "https://rickandmortyapi.com/api/character/1",
    "https://rickandmortyapi.com/api/character/2",
    ...
  ],
  "url": "https://rickandmortyapi.com/api/episode/28",
  "created": "2017-11-10T12:56:36.618Z"
}
"""

# can you use the URLs to make a subsequent call inside your for loops
# to replace the url with just the appropriate names?
# NOTE: need to make use of if statements to see if url exists or not
# (contact instructors for office hours if stuck!)

for row, episode in enumerate(data, 2):
  for column, episode in enumerate(episode.items(), 1):
      if episode[0] == "characters":
          # new list to collect the names
          # for loop for each character  
          # then do another request
          # deserialize for just the name       
          # append name to new list
          ws.cell(row=row, column=column, value=str(name_list))
      else:
        ws.cell(row=row, column=column, value=str(episode[1]))