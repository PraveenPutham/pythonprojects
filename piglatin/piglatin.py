import string

def convertasentencetopiglatin(words):
	final =  ''
	for word in words:
		final += convertawordtopigLatin(word) + ' '
	return final 

def convertawordtopigLatin (word):
	if (word[0] in ['a','e','i','o','u']):
		newword = word[0:]+'hay'
	else:
		newword = word[1:] +'ay'
	return newword


a = input('Get the text to convert to Pig latin:')
#print (a)
words = a.split(' ')
#print(len(words))

if (len(words)  > 1):
	print(convertasentencetopiglatin(words))
else:
	print(convertawordtopigLatin(words[0]))