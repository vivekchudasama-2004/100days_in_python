length=input("enter the list of length : ").split()
for i in range(0,len(length)):
    length[i]=int(length[i])
print(length)

highest_length=0
for leng in length:
    if leng>highest_length:
        highest_length=leng
print(leng)
    