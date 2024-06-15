programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."
}
#LOOP THROUGH DICTONARY
#reteriving data foem dictonary
for key, value in programming_dictionary.items():
    print(key)
    print(value)
    print(programming_dictionary["Bug"])
    print(f"{key}: {value}")
    print(programming_dictionary[key])
#adding data in dictonary
programming_dictionary["name"]="vivek"
print(programming_dictionary["name"])

#create empty dictonary
empty_dictonary={}

#wipe an extistance dictonary
#programming_dictionary={}

#edit an item in a dictonary
programming_dictionary["name"]="vrc"
print(programming_dictionary["name"])