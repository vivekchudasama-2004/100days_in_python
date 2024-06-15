def my_function():
    return 3*2
print(my_function())

#function with output
def formate_name():
    f_name = input("Enter your first name: ").title()
    l_name = input("Enter your last name: ").title()
    return f"{f_name}{l_name}"
print(formate_name())

#or

def formate_name(first_name, last_name):
    formate_f_name=first_name.title()
    formate_l_name=last_name.title()

    return f"{formate_f_name}{formate_l_name}"
print(formate_name("vivek","chudasama"))