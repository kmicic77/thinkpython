import turtle

def koch(t,x):
	""" draws Koch curve"""
	if x<3:
		t.fd(x)
		return
	else:
		koch (t,x/3)
		t.lt(60)
		koch (t,x/3)
		t.rt(120)
		koch (t,x/3)
		t.lt(60)
		koch (t,x/3)
def snowflake (t,x):
	for i in range(3):
		koch(t,x)
		t.rt(120)
		
bob=turtle.Turtle()
snowflake (bob,200)
turtle.mainloop()