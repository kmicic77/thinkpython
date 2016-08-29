from math import sqrt,factorial,pi
def estimate_pi():
	""" Esimates pi using Srinivasa Ramanujan formula """
	k=0
	estimate=0
	while True:
		estimate+=(2*sqrt(2)/9801)*(factorial(4*k)*(1103+26390*k))/(((factorial(k))**4)*396**(4*k))
		if abs(1/estimate-pi)<1e-15:
			print ("Estimate calculated for k=0 to k={}".format(k))
			return 1/estimate
		k+=1
print (estimate_pi())
		