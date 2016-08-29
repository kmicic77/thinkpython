import math
def mysqrt(a):
	""" looking for estimate of square root of number a """
	#x - reasonable estimate
	x=a/2
	
	epsilon=0.0001
	while True:
		y=(x+a/x)/2
		if abs(y-x)<epsilon: break
		x=y
	return y
def test_square_root():
	print("a   mysqrt(a)     math.sqrt(a)  diff")
	print("-   ---------     ------------  ----")
	for a in range(1,10):
		estimate=mysqrt(a)
		actual=math.sqrt(a)
		print("{:3.1f} {:13.11f} {:13.11f} {:13.11f}".format(a,estimate,actual,abs(actual-estimate)))
test_square_root()
	