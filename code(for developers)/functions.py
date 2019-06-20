import random

def update():
	file = open('newwords.txt')
	words = file.readlines()  #all file as a list of strings

	keys = []
	fullvalues = []
	values = []
	for word in words:
		if len(word) > 4 :
			word=word.strip()
			keys.append(word.split(':')[0])
			fullvalues.append(word.split(':')[1])
	file.close()
	for value in fullvalues:
		values.append(value.split(';'))
	#print(keys)
	#print(values)
	dictionary = {}
	for x in range(len(keys)):
		dictionary[keys[x]] = values[x]

	return dictionary

def add():
	condition = True
	while condition:
		word = input('Enter a word which you wanna add: ')
		meaning = input('Enter a meaning: \nseparate multiple meanings by ; like meaning1;meaning2 \n ')
		file = open('newwords.txt','a')
		file.write('\n' + word + ':' + meaning)
		file.close()
		nextword = input('Word was successfully added, hit + to add next word or \n press any other button and Enter to exit ')
		if nextword == '+':
			continue
		else:
			break
			


def remove():#ALMOST DONE
	myword = input('Enter a word which you wanna remove: ')
	file = open('newwords.txt','r')
	words = file.readlines()
	delimiter = ':'
	l = []   #list of tuples of word,meaning
	for word in words:
		if len(word) >= 4:
			word=word.strip()
			l.append(tuple(word.split(delimiter)))
	file.close()
	newdict = dict(l)
	if myword in list(newdict.keys()):
		del newdict[myword]
		#print(newdict) 
		write = open('newwords.txt','w')
		for x in newdict:
			write.write(x + ':' + newdict[x] + '\n')
		write.close()
		print(str(word)+' was successfully removed')



def show():#DONE
	file = open('newwords.txt','r')
	print('\n')
	for x in file:
		if x != '\n':
			print(x)

def move():
	pass
	#word = input('Enter a word which you wanna move: ')
	#answer = input('Enter - to move word to the oldwords and remove from current place: ')
	#if answer == '-':
	#	oldwords = open('oldwords.txt','a')
	#	oldwords.write(str(word) + ':' + str(dictionary[word]))
	#	oldwords.close()
	#	newwords = open('newwords.txt','r+')
	#	listOfNewWords = newwords.readlines()
	#	delimiter = ':'
	#	newl = []   #list of tuples of word,meaning
	#	for newword in listOfNewWords:
	#		newword = newword.strip()
	#		newl.append(tuple(newword.split(delimiter)))
	#	newdictionary = dict(newl)
	#	del newdictionary[word]
	#	newwords.write('\n')
	#	for key,value in newdictionary.items():
	#		newwords.write(str(key) + ':' + str(value) + '\n')

def match(word,meanings):
	for correct in meanings:
		length = len(correct) / 10 * 7
		if len(set(word) & set(correct)) >= length:
			return True
		#else:
		#	continue


def train(dictionary):
	print('write "stop" to leave a train')
	try:
		amount = int(input('How many words do you want to train?'))
		count = 0
		score = 0
		while amount > 0:
			word = random.choice(list(dictionary.keys()))
			print('word ' + word)
			answer = input('meaning: ')
			if match(answer,dictionary[word]):
				print('Correct')
				score += 1
				del dictionary[word]
			#if answer in dictionary[word]:
			#	print('Correct')
			#	score += 1
			#	del dictionary[word]
			elif answer =='stop':
				return update()
			else:
				print('Incorrect')
			amount -= 1
			count += 1
	except:
		print('You have guessed all words!')
		return update()
	print('Your score = ' + str(score) + ' of ' + str(count))
	return update()