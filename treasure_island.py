print("Welcome to Treasure Island.\n Your mission is to find the treasure.")

direction = input('You\'r at a crossroad, where do you want to go? Type "left" or "right".\n')

if (direction == "left"):
    cross = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat. Type "swim" to swim across.\n')
    if (cross == "wait"):
        door = input("You have arrived at the island unharmed. there is a house with 3 doors. One red, one yellow and one blue. Which door do you want to open?\n")
        if (door == "Red") or (door == "red"):
            print("It's a room full of fire. Game Over.")
        elif (door == "Blue") or (door == "blue"):
            print("You enter a room of beasts. Game Over.")
        elif (door == "Yellow") or (door == "yellow"):
            print("You found the treasure. You Win!")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by crocodile. Game Over.")
else:
    print("You fell into a well. Game Over.")

