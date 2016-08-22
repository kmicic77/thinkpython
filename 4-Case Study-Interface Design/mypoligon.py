import turtle
bob=turtle.Turtle()
def square(t,length):
	for i in range(4):
		t.fd(length)
		t.lt(90)
	turtle.mainloop()
def polygon(t,length,n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)
	turtle.mainloop()
# square(bob,400)
# polygon(bob,100,7)
def circle(t,r):
	n=round(2*3.14*r/5)
	polygon(t,5,n)
def arc(t,r,angle):
	proportion=angle/360
	n=round(proportion*2*3.14*r/10)
	for i in range(n):
		t.fd(10)
		t.lt(angle/n)
	turtle.mainloop()

arc(bob,100,240)

