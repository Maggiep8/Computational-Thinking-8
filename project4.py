# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
x1 = -250
y1 =  250
x2 = -200
y2 = 200
x3 = -150
y3 = 150
x4 = -100
y4 = 100
# Section 3 - Setup
set_background("summer")
t1 = create_sprite("dog",x1,y1)
t2 = create_sprite("flower",x2,y2)
t3 = create_sprite("softball",x3,y3)
t4 = create_sprite("bike",x4,y4)


# # Section 4 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
# for i in range(35):
x1 += 21
x2 += 50
x3 += random.randit (8,30)
x4 += random.randit (9,20)
t1.goto(x1, y1)
t2.goto(x2, y2)
t3.goto(x3, y3)
t4.goto(x4, y4)
time.sleep(0.1)


# # Section 5 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("player 1 wins!")


if x2 >= x1 and x2 >= x3 and x2>= x4:
	print("player 2 wins!")
if x3 >= x2 and x3 >= x4 x3 >= x1:
	print("player 3 wins!")
if x4 >= x1 and x4 >= x2 and x4 >= x3:
	print("player 4 wins")
	
	


turtle.exitonclick()
