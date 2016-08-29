import math
def eval_loop():
	while True:
		string=input("What do you want to calculate?>>>")
		if string=="done": break
		try:
			print (eval(string))
		except:
			print("It's not a valid input!")
eval_loop()
		