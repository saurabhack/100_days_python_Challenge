again=True
name=input("Enter your name = ").lower()
bid_price=int(input("bid price = "))
dictionary={}
dictionary[name]=bid_price
print("dictionary == ",dictionary)
restart=input("any one want to bid ? if yes please type yes otherwise type no = ").lower()
if(restart=="yes"):
    again=True
elif(restart=="no"):
    again=False
while(again == True):
    name=input("Enter your name = ").lower()
    bid_price=int(input("bid price = "))
    dictionary[name]=bid_price
    print("dictionary == ",dictionary)
    restart=input("any one want to bid ? if yes please type yes otherwise type no =\n ").lower()
    if(restart=="yes"):
        again=True
        print("\n"*100)
    elif restart=="no":
        again=False

def evaluation(dictionary):
    maximum=0
    winner=""
    for i in dictionary:
        bid_amount=dictionary[i]
        if maximum<dictionary[i]:
            maximum=bid_amount
            winner=i
    return winner
print("winner is = ",evaluation(dictionary))