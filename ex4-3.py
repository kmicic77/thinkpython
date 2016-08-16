import turtle
import math

def triangle (t,r,angle):
    t.fd(r)
    triangle_angle=((180-angle)/2)
	
    t.lt(180-triangle_angle)
    a=math.sqrt(2*r**2*(1-math.cos(angle*math.pi/180)))
    print (a)
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
figure (bob,5,100)
move(bob,220)
figure (bob,6,100)
move(bob,220)
figure (bob,7,100)

turtle.mainloop()