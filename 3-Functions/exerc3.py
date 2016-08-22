def right_justify(s):
	news=''
	for i in range(70-len(s)):
		news+=' '
	news+=s
	print (news)
	
right_justify('monty')