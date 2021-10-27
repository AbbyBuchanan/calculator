#group members: abby <3, amber <3, meena <3, katelyn <3


import turtle as trtl
t = trtl.Turtle()

t.speed(0)

#create the y and x axis
t.penup()
t.setposition(0,400)
t.pendown()
t.right(90)
t.forward(800)
t.penup()
t.setposition(-400,0)
t.pendown()
t.left(90)
t.forward(800)

#positive x line dashes
x_cor = 20
y_cor = 10

t.penup()
t.setposition(x_cor,y_cor)
t.pendown()

t.right(90)

for i in range(10):
  for i in range(2):
    t.forward(20)
    t.left(90)
    t.penup()
    t.forward(20)
    t.left(90)
    t.pendown()
  x_cor = x_cor + 40
  t.penup()
  t.setposition(x_cor, y_cor)
  t.pendown()

x_cor = 10
y_cor = 20

#positive y line dashes
x_cor = -10
y_cor = 20

t.penup()
t.setposition(x_cor, y_cor)
t.pendown()

t.left(90)

for i in range(10):
  for i in range(2):
    t.forward(20)
    t.left(90)
    t.penup()
    t.forward(20)
    t.left(90)
    t.pendown()
  y_cor = y_cor + 40
  t.penup()
  t.setposition(x_cor, y_cor)
  t.pendown()


#negative x line dashes (left)
x_cor = -20
y_cor = -10

t.penup()
t.setposition(x_cor, y_cor)
t.pendown()

t.left(90)

for i in range(10):
  for i in range(2):
    t.forward(20)
    t.left(90)
    t.penup()
    t.forward(20)
    t.left(90)
    t.pendown()
  x_cor = x_cor - 40
  t.penup()
  t.setposition(x_cor, y_cor)
  t.pendown()


#negative y line dashes (right)
x_cor = -10
y_cor = - 20

t.penup()
t.setposition(x_cor, y_cor)
t.pendown()

t.right(90)

for i in range(10):
  for i in range(2):
    t.forward(20)
    t.right(90)
    t.penup()
    t.forward(20)
    t.right(90)
    t.pendown()
  y_cor = y_cor - 40
  t.penup()
  t.setposition(x_cor, y_cor)
  t.pendown()

#asks for input
user_input = input("give me an y=mx+b equation")
slope = int(user_input[2])
yi = int(user_input[5])
yi = yi * 20

#draws line
t.speed(10)
t.penup()
t.setposition(0,yi)
x = 400
r = slope * x + yi
t.setposition(x,r)
t.pendown()
x=-400
l = slope * x + yi
t.setposition(x,l)


wn = trtl.Screen()
wn.mainloop()