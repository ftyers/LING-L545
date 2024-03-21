import sys, re
abbr = ['etc.', 'e.g.', 'i.e.']
alphabet = ",abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def tokenise(line):
	line = re.sub(r'([\(\)"?:!;])', r' \g<1> ', line)
	line = re.sub(r'([^0-9]),', r'\g<1> ,', line)
	line = re.sub(r',([^0-9])', r', \g<1>', line)
	line = re.sub(r'  *', r' ', line)

	tokens = []
	for char in line:
		if char == '':
			continue
		if char[-1] == '.' and char not in abbr:
			char = char[:-1] + ' .'
		try:
			if char == " ":
				pass
			else:
				if char in alphabet and tokens[len(tokens)-1][0] in alphabet:
					tokens[len(tokens)-1] = tokens[len(tokens)-1] + char
				else:
					tokens.append(char) 
		except:			
			tokens.append(char)
	return tokens

with open("original.txt") as file:
	for line in file.readlines():
		tokens = tokenise(line)
		print(' '.join(tokens), end = '')
	

