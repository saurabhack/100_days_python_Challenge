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
user_card=[]
computer_card=[]
is_game_over=False

for i in range(2):
    user_card.append(deal_card())
    computer_card.append((deal_card()))

user_score=calculate_score(user_card)
computer_score=calculate_score(computer_card)

print(f"Your cards: {user_card}, current score : {user_score}")
print(f"computer's first cards : {computer_card[0]}")

if user_score == 0 or computer_score==0 or user_score>21:
    is_game_over=True
else:
    input("Type 'Y to get another card t" )