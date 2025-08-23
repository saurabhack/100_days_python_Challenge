print("The Lost City Of Pythonia ")

player=input("Enter your name = ").lower()

print(f"Well come to the lost city of pythonia {player}")

is_start=input("Did you want to start this game ? Y or N = ").lower()

if(is_start=="y"):
    print("Congratualations you started this game ! best of luck .")
    print("Only those carrying the golden key may pass.")
    is_pass=input("Do you have a golden key pass ? Y or N  ").lower()
    print("pass",is_pass)
    if(is_pass=="y"):
        path=input('''Choose your path ? "dark tunnle" or "sunny garden"  ''').lower()
        if(path=="dark tunnle"):
            print("You meet a dragon ? game over try next time ")
        else:
            print("You are in the beautifull garden")
            gem=input('''Pick the correct gem to unlock me . "ruby", "emerald", "saphire" , if you don't want to choose anything you can enter "NO" only ''').lower()
            if(gem=="ruby"):
                print("Poison spread in the room . You are FAILLED !!")
                print(f"GAME OVER ! {player}")
            elif(gem=="emerald"):
                print("Congratualations Mapp Opened !!!")
                print(f"Congratualations ! You win this game ! {player}")
            elif(gem=="saphire"):
                print("the chest reveals half the treasure.")
                print(f"Good try ! {player} try again after second time !")
            else:
                print(f"Game Over ! please try again {player}.")
    elif(is_pass=="n"):
        print("sorry . you have no right to enter inside the gate !")    
else:
    print("As you wish ! thanks for visiting this game .")