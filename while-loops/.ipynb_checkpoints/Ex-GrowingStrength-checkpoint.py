# The player's power starts out at 5
power = 5

# Player's initial strength
print("The player's intial strength is %d. " % power)

# The player is allowed to keep playing as long as their power is over 10
while power < 10:
    print("You are still playing, because your power is %d " %power)

    power = power + 1

    print("Your increased power is %d " %power)

print("\nOh no, you have grown to strong, and you have been moved to next level of the game")