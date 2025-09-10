#final project :- tip calculator
print("Welcome to the tip calculator")
total_amount=int(input("What was the total bill ? "))
tip=int(input("How much tip would you like to give ? "))
split=int(input("How many people to split the bill? "))
percentage=tip/100
total_tip_amount=total_amount*percentage
total_bil=total_amount+tip
bill_per_person=round(total_bil/split,2)
print(f"Each person should pay: {bill_per_person}")