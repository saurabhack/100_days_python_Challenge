import random
numbers=[1,2,3,4,5,6,...,100]

computer_number=random.choice(numbers)

def compare_with_computer(u_number,c_number):
    if u_number==c_number:
        return True
    elif u_number<c_number:
        return "small"
    elif u_number>c_number:
        return "big"

def guessing_core():
    total_round=8
    while total_round!=0:
        print(f"remained rounds {total_round}")
        user_number=int(input("enter number"))
        if compare_with_computer(user_number,computer_number) == True :
            print("You successfully guesed the number of the computer ")
            break
        elif compare_with_computer(user_number,computer_number) == "big":
            print("The guessed number is greater than computer number ")
            total_round=total_round-1
        elif compare_with_computer(user_number,computer_number) == "small":
            print("The guessed number is less than computer number ")
            total_round=total_round-1
        elif total_round==1:
            print("You lose the game , please try again ")

guessing_core()