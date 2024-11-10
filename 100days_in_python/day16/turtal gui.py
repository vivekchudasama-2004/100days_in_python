from turtle import Turtle,Screen
#object=class
timmy=Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('blue')

my_screen=Screen()
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
print(my_screen.canvheight)

#object,=.method name
my_screen.exitonclick()
