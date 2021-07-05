# import json library
import json

def print_data(personal_info):

    for key, value in personal_info.items():
        print(key.title() + ":" + value)

# declare a empty list
person_list = []

# open a file using context manager
with open('/Users/saurabhvisal/Desktop/Python Programs/JSON-API/json-fake-data.json') as json_file:
    data = json.load(json_file)

    # loop through each item in the json and get the follwing data
    for item in data:
        name = item['name']
        email = item['email']
        balance= item['balance']

        # put all the data into dict
        person_dict = {
            'name':name,
            'email':email,
            'balance':balance
        }

        # append the dictionary data into list
        #person_list.append(person_dict)

        #print the list
        #print(person_list)
        print_data(person_dict)