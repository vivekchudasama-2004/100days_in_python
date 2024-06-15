hieght=input("enter the hight: ").split()
p = 0
for i in range(0,len(hieght)):
   hieght[i]=int(hieght[i])
print(hieght)

total_hight=0
for hieghts in hieght:
    total_hight+=hieghts
print(total_hight)

num_of_student=0
for student in hieght:
    num_of_student+=1
print(num_of_student)
averagehight=total_hight/num_of_student
print(averagehight)