#start
import turtle

t = turtle.Turtle()

turtle.Screen () .bgcolor("Black")

t.penup()
t.goto (-50,-100)
t.pendown()
#Colorchangeing, growingshape, rotating shape
colors = ["Blue","DeepPink", "DarkViolet" ]
for i in range (1000):
    t.color (colors[ i % 3 ] )
    t.forward (100 + i)
    t.left (61)
#exit
turtle.exitonclick()