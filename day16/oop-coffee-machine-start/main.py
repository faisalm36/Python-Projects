from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()


coffee = True
while coffee:
  coffeeOptions = menu.get_items()
  name = input(f"What would you like? {coffeeOptions}: ")
  if name == "off".lower():
    coffee = False
  elif name == "report".lower():
    moneyMachine.report()
    coffeeMaker.report()
  else:
   drinkChoice =  menu.find_drink(name)
   resourcesGood = coffeeMaker.is_resource_sufficient(drinkChoice)
   if resourcesGood:
    money = moneyMachine.make_payment(drinkChoice.cost)
    if money == True: 
      coffeeMaker.make_coffee(drinkChoice)


   
    


    


