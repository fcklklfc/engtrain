import commands
while True:
	file = open('newwords.txt')
	words = file.readlines()  #all file as a list of strings
	'''
	delimiter = ':'
	l = []   #list of tuples of word,meaning
	for word in words:
		word=word.strip()
		l.append(tuple(word.split(delimiter)))
	file.close()
	dictionary = dict(l) # dict of word:meaning
	print(dictionary)

	'''

	keys = []
	fullvalues = []
	values = []
	for word in words:
		if len(word) > 4:
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



	#print(dictionary)
	print('write down "help" and hit "Enter" to see list of commands')




	condition = commands.command_line(dictionary)
	if condition == 'exit':
		break





	






		




 

