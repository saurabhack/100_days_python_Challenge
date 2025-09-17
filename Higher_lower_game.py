import random

from game_data import data
A=""
B=""
index = random.randint(1, 51)
def greater_value(a,b):
    if a>b:
        return a
    else:
        return b
def create_questions(score):
    gameRepitation=0
    index = random.randint(1, 50)
    index2 = random.randint(1, 50)

    while(gameRepitation!=-1):
        if index==index2:
            index = random.randint(1, 51)
        A=f"{data[index]['name']}, A {data[index]['description']} , from {data[index]['country']}"
        B=f"{data[index2]['name']}, A {data[index2]['description']} , from {data[index2]['country']}"
        print("Compare A:",A)
        print("Against B:",B)

        user_input=input("Who has more followers ? : ").lower()
        a=data[index]['follower_count']
        b=data[index2]['follower_count']
        ans=greater_value(a,b)
        user_value=0
        if user_input=="a":
            user_value=a
        elif user_input=="b":
            user_value=b
        if user_value==ans:
            score+=1
            index = index2
            index2 = random.randint(1, 50)
        elif user_value!=ans:
            break
    return score

current_score=create_questions(0)

print("Your current score is = ",current_score)