#conditional statement
#if else statement
print("Welcome to rollercoaster!")
height=int(input("What is your hieght in cm?"))
bill=0

if height>=120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age! "))
    if age<=12:
        print("child tickets are $5")
        bill=5
    elif age <= 18:
        print("youth tickets are $7")
        bill=7
    elif age>=45 and age<=55:
        print("Everything is going to be ok. have a free ride to us!")
    else:
        print("Adult tickets are $12")
        bill=12
    
    wants_photo=input("Do you want to have a photo take ? type y for yes and n for no. ")
    if wants_photo=="y":
         bill=bill+3
    print(f"Your final bill is {bill}")

else:
    print("sorry you have to grow taller you can ride.")

#modulo operator
#check number is even or odd

# number=int(input("Enter number="))
# if(number%2==0):
#     print("Number is even")
# else:
#     print("Number is Odd")

#Nested if else statement

