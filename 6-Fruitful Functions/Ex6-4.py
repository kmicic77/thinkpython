def is_power(a,b):
	""" checks if a is power of b """
	if a==b: return True
	if a<b: return False
	return (a%b==0 and is_power(a/b,b))
print (is_power(32,3))
print (is_power(81,3))
		