print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************" 
''')

print("Welcome to treasure Island.")
print("Your mission is to find treasure.")
choice1=input('You\re at crossroad, where do you want to go? Type "Left" Or "Right" .').lower()
if(choice1=='left' ):
    choice2=input('''You've come to a lake. there is an island in the middle of the lake. type "Wait" to wait for boat. type "Swim" to swim across.''')
    if choice2=="wait":
       choice3=input("You arrive at the island unbarmed. there is house with 3 doors. one red, one yellow and blue. which color do you choose?").lower()
       if choice3=="red":
           print("It's a room full of fire. Game Over")
       elif choice3=="Yellow":
           print("You found the treasure. You Win!")
       elif choice3=="blue":
           print("You enter a room of beasts. Game Over.")
       else:
           print("You coose door that doesn't exist. Game Over.")

    else:
        print("You get attracted by an angry trout. Game Over.")
else:
    print("You fall in on hole. Game Over.")



