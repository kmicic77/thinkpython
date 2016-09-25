def uses_all(word,required):
	for letter in required:
		if letter not in word:
			return False
	return True

required=input('Enter string of letters to find words containing them at least once each: ')
counter=0
with open('words.txt') as f:
	for line in f:
		word=line.strip()
		if uses_all(word,required):
			print (word)
			counter+=1
print('Number of words containing all those letters: {}'.format(counter))