import turtle
import math
""" draw 3 'sliced' polygons using general functions"""
def triangle (t,r,angle):
    #r - leg of isosceles triangle
    t.fd(r)
    triangle_angle=((180-angle)/2)
	
    t.lt(180-triangle_angle)
#a - base of isosceles triangle
    a=math.sqrt(2*r**2*(1-math.cos(angle*math.pi/180)))
    t.fd(a)
    t.lt(180-triangle_angle)
    t.fd(r)
def figure (t,n,r):
	for i in range(n):
		triangle (t,r,360/n)
		t.lt(180)
def move (t,length):
		t.pu()
		t.fd(length)
		t.pd()
		
bob=turtle.Turtle()
move (bob,-200)
figure (bob,5,100)
move(bob,220)
figure (bob,6,100)
move(bob,220)
figure (bob,7,100)

turtle.mainloop()