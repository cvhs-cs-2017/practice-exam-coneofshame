"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle

def square():
    MRthoe = turtle.Turtle()
    for i in range(4):
        MRthoe.fd(150)
        MRthoe.rt(90)
square()
