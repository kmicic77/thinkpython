def gcd(a,b):
	""" calculates greatest common divisor """
	if b==0: return a
	else: return gcd(b,a%b)
	
print (gcd(54,27))
