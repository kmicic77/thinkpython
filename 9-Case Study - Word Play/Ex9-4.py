def uses_only(word,available):
	for letter in word:
		if letter not in available:
			return False
	return True

available=input('Enter string of letters to find words containing only them: ')
counter=0
with open('words.txt') as f:
	for line in f:
		word=line.strip()
		if uses_only(word,available):
			print (word)
			counter+=1
print('Number of words containing only those letters: {}'.format(counter))