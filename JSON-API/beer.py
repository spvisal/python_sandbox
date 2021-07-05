import json
import pandas as pd
import sqlite3

conn = sqlite3.connect('food.db')
c = conn.cursor()

# c.execute(''' CREATE TABLE beer (name TEXT, tagline TEXT, first_brewed TEXT, description TEXT, 
#                 abv REAL, ph REAL, yeast TEXT, brewers_tips TEXT, contributed_by TEXT) ''')

with open('/Users/saurabhvisal/Desktop/Python Programs/JSON-API/beer.json') as json_file:
    json_data = json.load(json_file)

    for item in json_data:
        name = item['name']
        tagline = item['tagline']
        first_brewed = item['first_brewed']
        description = item['description']
        abv = item['abv']
        ph = item['ph']
        try:
            yeast = item['yeast']
        except:
            yeast = ''
        brewers_tips = item['brewers_tips']
        contributed_by = item['contributed_by']

        c.execute(''' INSERT INTO beer VALUES (?,?,?,?,?,?,?,?,?)''', (name, tagline, first_brewed, description, 
                 abv, ph, yeast, brewers_tips, contributed_by))

conn.commit()
print('Complete...')
