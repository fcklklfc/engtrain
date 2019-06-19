import functions





commands_list = {
	'move':'moves word to the oldwords and removes it from newwords',
	'remove':'removes word from newwords',
	'show':'shows all words from newwords',
	'exit':'exit',
	'add':'adds a words to the list',
	'train':'runs a training game',
	'help':'shows a list of commands'
}
def command_line(dictionary):
	while True:
		command = input('Enter your command: ')
		if command == 'exit':
			return 'exit'
		elif command == 'move':
			functions.move()
		elif command == 'help':
			for command,description in list(commands_list.items()):
				print(command + ' = ' + description)
		elif command == 'add':
			functions.add()
			return functions.update()

		elif command == 'remove':
			functions.remove()
		elif command == 'print':
			continue
		elif command == 'show':
			functions.show()
		elif command == 'train':
			return functions.train(dictionary)

