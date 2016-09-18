def is_palindrome(word):
	return word==word[::-1]

print ("Palindromes?")
words=['banana','pop','rotor','bread']
for word in words:
	print ('{} : {}'.format(word,is_palindrome(word)))
