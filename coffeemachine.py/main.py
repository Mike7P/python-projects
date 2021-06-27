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
def checklatte(ingredients):
    if ingredients['water'] > 200:
        global resources
        resources['water'] = resources['water'] - 200
    else: print(f'Sorry there is not enough water.')
    if ingredients['milk'] > 150:
        resources['milk'] = resources['milk'] - 150
    else: print(f'Sorry there is not enough milk.')
    if ingredients['coffee'] > 24:
        resources['coffee'] = resources['coffee'] - 24
    else: print(f'Sorry there is not enough coffee.')

def checkespresso(ingredients):
    if ingredients['water'] > 50:
        global resources
        resources['water'] = resources['water'] - 50
    else: print(f'Sorry there is not enough water.')
    if ingredients['coffee'] > 18:
        resources['coffee'] = resources['coffee'] - 18
    else: print(f'Sorry there is not enough coffee.')

def checkcappuccino(ingredients):
    if ingredients['water'] > 250:
        global resources
        resources['water'] = resources['water'] - 250
    else: print(f'Sorry there is not enough water.')
    if ingredients['milk'] > 100:
        resources['milk'] = resources['coffee'] - 100
    else: print(f'Sorry there is not enough milk.')
    if ingredients['coffee'] > 24:
        resources['coffee'] = resources['coffee'] - 24
    else: print(f'Sorry there is not enough coffee.')


def total(n, q, d, p):
    money = 0
    money = (n * 0.50) + (q * 0.25) + (d * 0.10) + (p * 0.1)
    return money
user_input = False
while user_input == False:
# print(MENU['latte']['cost'])
# TODO: 1. welcome statement - What would you like? (espresso/latte/cappuccino):
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
# TODO: 2. Create buckets money_input. + Change


# TODO: 3. Create functions for each drink to should check ingredients and remove the amount from the resor.
# it needs to return if out print(Sorry there is not enough {resource}.


# TODO: 5. Create IF statements to choose which function to call. Also one that prints report.
    if choice == 'report':
        print(resources)
        continue
    elif choice == 'espresso':
        checkespresso(resources)
    elif choice == 'latte':
        checklatte(resources)
    elif choice == 'cappuccinno':
        checkcappuccino(resources)
    nickles = 0
    quarters = 0
    dimes = 0
    pennies = 0

    nickles = float(input('how many nickles?: '))
    quarters = float(input('how many quarters?: '))
    dimes = float(input('how many dimes?: '))
    pennies = float(input('how many pennies?: '))
# TODO: 6. Print(Please insert coins.) Then create 4 input Q. how many quarters?: how many dimes?: how many nickles?:
# how many pennies?: thenn a function to add up the total
    total = total(nickles, quarters, dimes, pennies)
    change = round(total - MENU[choice]['cost'], 2)
# TODO: 7. Create function to add up the 4 amounts and compare to price. Return change or print statement
    if MENU[choice]['cost'] > total:
        print("Sorry that's not enough money. Money refunded.")
        user_end = True
    elif MENU[choice]['cost'] <= total:
        print(f"Here is ${change} in change. Here is your latte ☕️. Enjoy!")

#  If Under print(Sorry that's not enough money. Money refunded.)
#  If equal or over print(f"Here is ${change}in change. & print(Here is your latte ☕️. Enjoy!")
# loop back to beginning

#  TODO: 9. Loop back to start
