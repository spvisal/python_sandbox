# import required packages
import json
import requests
import random 


# get the parameter from the user
food_choice = input('Please enter your food choice: ')

# url to hit and get the response
url = f'https://api.punkapi.com/v2/beers?food={food_choice}'

# get the respose in a variable
response = requests.get(url)

# load the response in json format
data = json.loads(response.text)

beer_list = []

# loop through the response and collect the information what we need
for beer in data:
    name = beer['name'],
    tagline = beer['tagline']
    abv = beer['abv']

    # create a dict to hold the data
    beer_dict = {
        'name': name,
        'tagline':tagline,
        'abv':abv
    }

    beer_list.append(beer_dict)

value = random.randint(0, len(beer_list))
try_this = beer_list[value]

try_name = try_this['name']
try_tagline = try_this['tagline']
try_abv = try_this['abv']

print(f'You should try {try_name}, {try_tagline}. It has got {try_abv} % alcohol')