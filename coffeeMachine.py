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


user_input=input("What would you like ? (espresso/latte/cappuccino): ")

def total_of_coins():
    quarters=int(input("How many quarters: "))
    dimes=int(input("How many dimes: "))
    nickles=int(input("How many nickles: "))
    pennies=int(input("How many pennies: "))
    total=(quarters*0.25)+(dimes*0.10)+(nickles*0.5)+(pennies*0.1)
    return total

def for_coffee(resources,user_input):
    print("please insert the coins")
    value=total_of_coins()
    print(value)
    if value < MENU["latte"]["cost"] :
        print("Sorry that's not enough money. Money refunded")
        return False
    elif value>=MENU["latte"]["cost"]:
        if MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["latte"]["ingredients"]["water"] == \
                resources["water"]:
            print(f"Here is your latte. {user_input}!")
            return True
        elif MENU["latte"]["ingredients"]["water"] > resources["water"] and MENU["latte"]["ingredients"]["water"] != \
                resources["water"]:
            print("sorry we have no enough resource !")
            return False





if(user_input=="report"):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")

else:
    pass


print(for_coffee(resources,user_input))
