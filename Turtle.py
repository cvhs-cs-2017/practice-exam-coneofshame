""" Create a Turtle, name it, make it BLUE and draw a Smiley Face"""
import turtle

thoe = turtle.Turtle()

thoe.up()
thoe.lt(90)
thoe.fd (200)
thoe.rt(270)
thoe.down()
thoe.begin_fill()
thoe.color('blue')
thoe.circle(200,360)
thoe.end_fill()
thoe.up
thoe.goto(75,50)
thoe.color('yellow')
thoe.down()
thoe.begin_fill()
thoe.rt(180)
thoe.circle(50, 360)
thoe.end_fill()
thoe.up()
thoe.bk(150)
thoe.down()
thoe.begin_fill()
thoe.circle(50,360)
thoe.end_fill()
thoe.up()
thoe.rt(90)
thoe.fd(50)
thoe.rt(90)
thoe.fd(75)
thoe.lt(90)
thoe.down()
thoe.circle(150, 180)


from Myfile import polygon
turtle.clearscreen()
polygon(10)
