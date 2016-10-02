def three_double_letters(word):
	if len(word)<6:
		return False
	for i in range(len(word)-5):
		if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
			return True
	return False



counter=0
with open('words.txt') as f:
	for line in f:
		word=line.strip()
		if three_double_letters(word):
			print (word)
			counter+=1
print('Number of words with three consecutive double letters: {}'.format(counter))