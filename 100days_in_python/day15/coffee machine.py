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

total=0

def formate_data(item_cost):
    cost=item_cost["cost"]
    return cost[""]["cost"]
def trancaction():
    total = 0
    print("please insert a coin")
    total=int(input("how many quarters :"))*0.25
    total+=int(input("how many dimes :"))*0.1
    total+=int(input("how many nickles :"))*0.05
    total+=int(input("how many pennies :"))*0.01
    return print(total,"$")

new_order=True


while new_order:
    get_item=input("what would you like? (espresso/latte/cappuccino): ").lower()
    if get_item == "report":
        for key, value in resources.items():
            print(key + ": " + str(value))
    elif get_item=="off":
        new_order=False
    if get_item=="total":
        trancaction()
print(MENU["espresso"]["cost"])

