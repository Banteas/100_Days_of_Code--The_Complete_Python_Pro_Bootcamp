print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
turn = input("You are in a cross road, where do you want to go, left or right?: ").lower()
if turn == "right":
    print("Fall into a hole.Game Over.")
elif turn == "left":
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake."
                     "You want to wait for a boat or swim across?: ").lower()
    if swim_or_wait == "swim":
     print("Attacked by trout. Game Over.")
    elif swim_or_wait == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. "
                       "red/yellow/blue. Which one do you choose?: ").lower()
        if door == "red":
            print("Burned by fire.Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You Win!!")
        else:
            print("Wrong option..")
    else:
        print("Wrong choice. Game over")

else:
    print("Wrong answer. Game over")