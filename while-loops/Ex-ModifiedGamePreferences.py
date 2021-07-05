# Start with an empty list. You can 'seed' the list with
# some predefine values if you like.

games = ["football", "cricket", "tenis"]

# Set the new_game to something other than quit
new_game = ''

# Start a loop that will run until user enters 'quit'
while new_game != 'quit':
    # Ask the user for new game
    new_game = input("Please enter the game of your choice ")

    # Add the new game to our list only of it is not quit
    if new_game != 'quit':

        # Check if the game is already their in the list or not and then only add to list.
        is_available = new_game in games
        if is_available == False:
            games.append(new_game)
        else:
            print("You are trying to add " + new_game + " is already available..Please add another game..")

# Show that new game has been added.
print(games)