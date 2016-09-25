def is_abecedarian(word):
	previous=word[0]
	for c in word:
		if c<previous:
			return False
		previous=c
	return True
counter=0
with open('words.txt') as f:
	for line in f:
		word=line.strip()
		if is_abecedarian(word):
			print (word)
			counter+=1
print('Number of abecedarian words: {}'.format(counter))