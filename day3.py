print('''
*******************************************************************************
          |                   |                  |                     |
 ________|.="";=.||______
|                   |  ,-"_,=""     `"=.|                  |
||"=._o`"-.        `"=.|___________________
          |                "=._o"=._      `"=.                     |
 ________|:=.o "=..".-="'"=.|______
|                   |    _.--" , ; `"=._o." ,-"""-. ".   |
||."  ,. .` ` `` ,  `"-."-._   ". '|___________________
          |           |o`"=.` , "` `; .". ,  "-."-._; ;              |
 ________|| ;-.o"=._; ." ` '."\ . "-._ /|______
|                   | |o;    "-.o"=.``  '` " ,_.--o;   |
||| ;     (#) `-.o `"=.`_.--"o.-; ;|___________________
___///|o;._    "      `".o|o_.--"    ;o;///____
////"=._o--.        ; | ;        ; ;////_
___////"=._o--.   ;o|o;     .;o;///____
/////"=.o.; | ;.--"o.--"////_
___/////"=.o|o_.--""////___
///////////_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("You're at a crossroad. Where do you want to go?left or right")
direction = input("left or right?")
if direction == "left":
  where = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
  if where == "wait":
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
    if door == "red":
      print("It's a room full of fire. Game Over.")
    elif door == "yellow":
      print("You found the treasure! You Win!")
    elif door == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
