import turtle

wd = turtle.Screen()
wd.title("Pong 1.0 by alex-_-")
wd.bgcolor("black")
wd.setup(width=900, height=600)
wd.tracer(0)
# padelA
padella = turtle.Turtle()
padella.shape("square")
padella.penup()
padella.speed(0)
padella.shapesize(stretch_len=0.4, stretch_wid=5.5)
padella.goto(-350, 0)
padella.color("white")

# padelb
padellb = turtle.Turtle()
padellb.shape("square")
padellb.penup()
padellb.speed(0)
padellb.shapesize(stretch_len=0.4, stretch_wid=5.5)
padellb.goto(350, 0)
padellb.color("white")
# palla

palla = turtle.Turtle()
palla.shape("square")
palla.penup()
palla.speed(0)
palla.goto(0, 0)
palla.shapesize(stretch_len=0.7, stretch_wid=0.7)
palla.color("white")


# movimenti
def padel_a_up():
    y = padella.ycor()
    y += 20
    padella.sety(y)


def padel_a_down():
    y = padella.ycor()
    y -= 20
    padella.sety(y)


def padel_b_up():
    y = padellb.ycor()
    y += 20
    padellb.sety(y)


def padel_b_down():
    y = padellb.ycor()
    y -= 20
    padellb.sety(y)


# keyboard
wd.listen()
wd.onkeypress(padel_a_up, "w")
wd.onkeypress(padel_a_down, "s")
wd.onkeypress(padel_b_up, "Up")
wd.onkeypress(padel_b_down, "Down")

while True:
    wd.update()
