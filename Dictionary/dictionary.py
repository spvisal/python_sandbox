#check whether user requested key is available in the dictionary or not?
mountains = { 'mount everest': {'metres': '8,848', 'feet': '29,029', 'range':'Himalayas'},
             'K2':{'metres': '8,611', 'feet': '28,251', 'range':'Karakoram'}
}

print("What would you like to know about top 2 mountains in the world?")

requested_key = ''

while requested_key != 'quit':
    requested_key = input("Please enter the key that you want to search?- ")
    if requested_key != 'quit':
        for key_name, key_value in mountains.items():
            print(key_name.title())
            for nested_key_name, nested_key_value in key_value.items():
                if key_name == requested_key:
                    print(" " + f"{nested_key_name}: {nested_key_value}")
        break
    else:
        print("bye..")
