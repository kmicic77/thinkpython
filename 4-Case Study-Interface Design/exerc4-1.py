from polygon import arc
import turtle

bob=turtle.Turtle()
def petal(t,r,angle):
	for i in range(2):
		arc (t,r,angle)
		t.lt(180-angle)
	
	
def flower(t,n,r,angle):
    for i in range(n):
	    petal(t,r,angle)
	    t.lt(360.0/n)

flower(bob,10,100,60)
turtle.mainloop()