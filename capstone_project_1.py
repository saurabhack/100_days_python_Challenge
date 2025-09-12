import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21  and len(cards)==2:
        return 0
    if 11 in cards and sum(cards):
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, opponent has Blackjack "
    elif user_score>21:
        return "You went over. You lose"
    elif computer_score>21:
        return "Opponent went over. You win"
    elif user_score>computer_score:
        return "You Win"
    else:
        return "You lose"


def play_game_aggain():
    user_card=[]
    computer_card=[]
    is_game_over=False

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append((deal_card()))

    while not is_game_over :
            
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)

        print(f"Your cards: {user_card}, current score : {user_score}")
        print(f"computer's first cards : {computer_card[0]}")

        if user_score == 0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal= input("Type 'Y to get another card type 'n' to pass : " )
            if user_should_deal=="Y":
                user_card.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<12:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)



    print(f"Your final hand: {user_card}, final score: {user_score}")

    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score,computer_score))

is_play=input("Do you want to play Game Of Blackjack? Type 'y' or 'n' :")

while is_play=="y":
    print("\n"*20)
    play_game()