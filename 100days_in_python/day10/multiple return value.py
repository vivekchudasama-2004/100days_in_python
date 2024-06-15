def name(f_name,l_name):
    if f_name =="" or l_name=="":
        return "you did't provide input."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(name(input("enter your first name"),input("enter your last name")))