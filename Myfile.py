import turtle

def polygon(n):
    n = int(n)
    doodle = turtle.Turtle()
    theta = 360 / n
    for i in range(n):
        doodle.fd(50)
        doodle.rt(theta)
