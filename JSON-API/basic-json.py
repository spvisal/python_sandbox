# import json library
import json

# open a file using context manager

with open('/Users/saurabhvisal/Desktop/Python Programs/JSON-API/json-fake-data.json') as json_file:
    data = json.load(json_file)

    # accessing the data from the json
    # print(data[0]['name'])
    # print(data[0]['email'])
    # print(data[0]['balance'])
    # # access the tags key, it will actually return a list containtaing a values within
    # print(data[0]['tags'])

    # in case we want to store this information in a dictonary
    # name = data[0]['name']
    # email = data[0]['email']
    # balance = data[0]['balance']
    # tags = data[0]['tags']

    for item in data:
        name = item ['name']
        # create a dictinoray
        person_info = {
            'name': name
            # 'email': email,
            # 'balance':balance,
            # 'tags': tags
        }

    # print the dict
    print(person_info)
    