import random
numbers=list(range(1, 101))
level_of_game=input("Choose a difficulty  . Type 'easy' or 'hard' .")
attempts=0
if level_of_game=="easy":
    attempts=10
elif level_of_game=="hard":
    attempts=5
computer_selected_number=random.choice(numbers)
print("computer selected number = ",computer_selected_number)
while attempts!=0:
    print(f"You have {attempts} Attempts remaining")
    user_input_number=int(input("Make a guess: "))
    if(user_input_number<computer_selected_number):
        print("Too low.")
    elif(user_input_number>computer_selected_number):
        print("Too high")
    elif(user_input_number==computer_selected_number):
        print("You win!")
        break
    attempts-=1

if(attempts==0):
    print("You Lose the game!")