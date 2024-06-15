import random
name_string = input("give me everybody's names , who are going to pay bill :")
name=name_string.split(",")
length_of_name_string=len(name)
random_name=random.randint(0,length_of_name_string-1)
person=name[random_name]
print(f"{person} is going to pay bill")