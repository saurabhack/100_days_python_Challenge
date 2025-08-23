import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scisore='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

gameList=[]
gameList.append(rock)
gameList.append(paper)
gameList.append(scisore)
userInput=int(input("What do you choose ? Type 0 for rock, 1 for paper, 2 for scissors  ="))

print("You chose :-")
if userInput>=0 and userInput<=2:
    print(gameList[userInput])
computer_choice=random.randint(0,2)
print("Computer Choose :")
print(gameList[computer_choice])
if userInput>=3 or userInput<0:
    print("You typed invalid number. You lose")
elif computer_choice>userInput:
    print("You lose!")
elif userInput > computer_choice:
    print("You win!")
elif computer_choice==0 and userInput==2:
    print("You lose!")
elif userInput == 0 and computer_choice==2:
    print("You Wins!")
elif computer_choice==userInput:
    print("It's a draw")