#add only even numbers
total=0
for i in range(2,101,2):
    total+=i
print(total)

add=0
for n in range(1,101):
    if n%2==0:
        add+=n
print(add)
