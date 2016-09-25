def avoids(word,forbidden):
	for letter in word:
		if letter in forbidden:
			return False
	return True

forbidden=input('Enter string of forbidden letters: ')
counter=0
with open('words.txt') as f:
	for line in f:
		word=line.strip()
		if avoids(word,forbidden):
			print (word)
			counter+=1
print('Number of words without those letters: {}'.format(counter))