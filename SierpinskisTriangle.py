import turtle
import random
import math
import time

t=turtle.Turtle()
s=turtle.Screen()
t.speed(0)
t.hideturtle()
##t.tracer(0,0)
##s.delay(1000)
s.tracer(0,0)

def triangle(length):
   for i in range (0,3):
      t.forward(length)
      t.left(120)
   if update in ['y','Y','yes','Yes']:
      s.update()

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
      t.up()
      t.fd(length/2)
      t.down()
      sierpinski(num-1,length/2)
      t.up()
      t.bk(length/2)
      t.left(60)
      t.fd(length/2)
      t.right(60)
      t.down()
      sierpinski(num-1,length/2)
      t.up()
      t.right(120)
      t.fd(length/2)
      t.left(120)
      t.down()

num=input("Enter number of recursions: ")
length=input("Enter length of triangle: ")
update=raw_input("Do you want to update per triangle?: ")
t.up()
t.back(length/2)
t.right(90)
t.fd(length*math.sqrt(3)/4)
t.left(90)
t.down()
start_time=time.time()
sierpinski(num,length)
time=time.time()-start_time
s.update()
print("%f seconds required to make Sierpinski's Triangle to the %d degree and side length of %d"%(time,num,length),)
##print((time.time()-start_time),"seconds required to make Sierpinski's Triangle to the ",num," degree and side length of",length)
