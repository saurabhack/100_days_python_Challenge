MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

counter=0
while counter != 1:

    new_resources={}

    user_input=input("What would you like ? (espresso/latte/cappuccino): ")

    def total_of_coins():
        quarters=int(input("How many quarters: "))
        dimes=int(input("How many dimes: "))
        nickles=int(input("How many nickles: "))
        pennies=int(input("How many pennies: "))
        total=(quarters*0.25)+(dimes*0.10)+(nickles*0.5)+(pennies*0.1)
        return total

    def is_enough_resources(order,resources):
        for i in MENU[order]["ingredients"]:
            print(f"for loop from is_enough_resources functions == ", MENU[order]["ingredients"][i])
            if resources[i]<MENU[order]["ingredients"][i]:
                print("resources from is_enough resources==",resources[i])
                return resources[i]
        return True
    def use_of_resources(order,resources):
        for i in MENU[order]["ingredients"]:
            resources[i]-=MENU[order]["ingredients"][i]
        return resources


    def for_coffee(userInput):
        total_amount=total_of_coins()
        if total_amount<MENU[userInput]["cost"]:
            print("Sorry , you have not enough money")
            return False
        elif total_amount>=MENU[userInput]["cost"]:
            if is_enough_resources(userInput,resources)!=True:
                print(f"Sorry we have not enough resources to make the your coffee {userInput}")
                return False
            elif is_enough_resources(userInput,resources)==True:
                new_resources=use_of_resources(userInput,resources)
                print(f"Enjoy your {userInput}")
                return new_resources

            
    if(user_input=="report"):
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")

    else:
        new_resources=for_coffee(user_input)