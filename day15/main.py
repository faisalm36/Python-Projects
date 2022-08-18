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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coins = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}
def coins():
    # returns the total coins calculated from the coins inserted
    print("Please insert coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def resourceSufficient(orderIngredients):
    # returns true when an order is made and false if the ingredients are insufficient
    for item in orderIngredients:
        if orderIngredients[item] <=resources[item]:
            print(f"Sorry there is not enough water {item}")
            return False
    return True
def isTransactionSuccessful(moneyRecieved, drinkCost):
    # returns true when payment is accepted or false  if the money is insufficient
    if moneyRecieved >= drinkCost:
        change = round(moneyRecieved - drinkCost,2 )
        print(f"here is your money in change {change}")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry that is not enough money. Money refunded")
        return False
def makeCoffee(drinkName, orderIngredients):
    #deducts the required ingredients from the resources
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"here is your {drinkName}")




coffee = True
while coffee:
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffeeChoice ==  "off":
        coffee = False
    elif coffeeChoice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"cost: ${profit}")
    else:
        drink = MENU[coffeeChoice]
        if resourceSufficient(drink["ingredients"]):
             payment = coins()
             if isTransactionSuccessful(payment,drink["cost"]):
                 makeCoffee(coffeeChoice, drink["ingredients"])

