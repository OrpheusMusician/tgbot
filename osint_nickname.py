import os
def nickname(name):
	req = 'python osint_sherlock/sherlock/sherlock.py ' + name
	os.system(req)

def converting(filename):
	msg, n = '', 0
	messages = ['']
	with open(filename, 'r', encoding = "utf-8") as f:
		for line in f:
			n += 1
			if (line.find('Total Websites') != -1):
				msg = msg + '\nTotal Websites: ' + line[line.find(':') + 2 : len(line)]
			else:
				splitter = line.find(':')
				msg = msg + f'[{line[0 : splitter - 1]}]: {line[splitter + 2 : len(line)]}'

			if (n == 20):
				msg = msg.replace('Academia.edu', 'Academia Edu', 1) if (msg.find('Academia.edu') != -1) else msg
				msg = msg.replace('Repl.it', 'Repl It', 1) if (msg.find('Repl.it') != -1) else msg

				messages.append(msg)
				n = 0
				msg = ''

		else:
			if (messages[-1] != msg):
				msg = msg.replace('Academia.edu', 'Academia Edu', 1) if (msg.find('Academia.edu') != -1) else msg
				msg = msg.replace('Repl.it', 'Repl It', 1) if (msg.find('Repl.it') != -1) else msg

				messages.append(msg)
				n = 0
				msg = ''

	messages = messages[1 : len(messages)]
	# msg = msg.replace('.', '\.').replace('(', '\(').replace(')', '\)').replace('=', '\=').replace('!', '\!')
	os.remove(filename)
	return messages