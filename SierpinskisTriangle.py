import turtle
import random
import math
t=turtle.Turtle()
t.speed(0)
t.hideturtle()

def triangle(length):
   for i in range (0,3):
      t.forward(length)
      t.left(120)

def go(x,y):
   t.penup()
   t.goto(x,y)
   t.pendown()

##def sierpinski(num,length):
##   for i in range (0,3):
##      t.forward(length)
##      t.left(120)
##   length=length/2
##   go(length,length)
##   triangle(length)
##   for j in range (0,num):
##      triangle(length)
##      length=length/2
##      go(length,length)

def sierpinski (num,length):
   if num==0:
      triangle(length)
   else:
      sierpinski(num-1,length/2)
      t.fd(length/2)
      sierpinski(num-1,length/2)
      t.bk(length/2)
      t.left(60)
      t.fd(length/2)
      t.right(60)
      sierpinski(num-1,length/2)
      t.right(120)
      t.fd(length/2)
      t.left(120)

num=input("Enter number of recursions: ")
length=input("Enter length of triangle: ")
t.up()
t.back(length/2)
t.right(90)
t.fd(length*math.sqrt(3)/4)
t.left(90)
t.down()
sierpinski(num,length)
