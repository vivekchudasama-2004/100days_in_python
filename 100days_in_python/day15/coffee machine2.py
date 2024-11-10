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


def is_resourse_sefficient(order_ingredients):
    """return truy if resourses is sufficient else false"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coin():
    """return the total calculated from coin inserted """
    print("please insert a coin")
    total = int(input("how many quarters :"))*0.25
    total += int(input("how many dimes :"))*0.1
    total += int(input("how many nickles :"))*0.05
    total += int(input("how many pennies :"))*0.01
    return total


def is_transaction_succfull(money_received, drink_cost):
    """return true when the payment is accepted,
    or false if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"hear is ${change} in change")
        global profit
        profit += money_received
        return True
    else:
        print("sorry that's not enough money.Money refunded")
        return False


def make_a_coffee(drink_name, order_ingredients):
    """deduct the required ingerident from the resourses"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"hear is {drink_name}")


is_on = True

while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water:{resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee:{resources['coffee']}")
        print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        if is_resourse_sefficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_succfull(payment, drink["cost"]):
                make_a_coffee(choice, drink["ingredients"])
