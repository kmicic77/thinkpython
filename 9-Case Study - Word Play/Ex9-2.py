def has_no_e(word):
	for letter in word:
		if letter.lower()=='e':
			return False
	return True

with open('words.txt') as f:
	counter=0
	lines=0
	for line in f:
		lines+=1
		word=line.strip()
		if has_no_e(word):
			print (word)
			counter+=1
print ('Total words without \'e\':{}. It\'s {:.2f}% of all words'.format(counter,(counter/lines)*100))

