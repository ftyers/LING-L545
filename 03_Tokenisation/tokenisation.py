import sys, re
abbr = ['etc.', 'e.g.', 'i.e.']

def tokenise(line, abbr):
	line = re.sub(r'([\(\)"?:!;])', r' \g<1> ', line)
	line = re.sub(r'([^0-9]),', r'\g<1> ,', line)
	line = re.sub(r',([^0-9])', r', \g<1>', line)
	line = re.sub(r'  *', r' ', line)

	tokens = []
	for token in line.strip().split(' '):
		if token == '':
			continue
		if token[-1] == '.' and token not in abbr:
			token = token[:-1] + ' .'
		tokens.append(token)
	return tokens

line = sys.stdin.readline()
while line:
	tokens = tokenise(line, abbr)
	print(' '.join(tokens), end = "")
	line = sys.stdin.readline()
	if not line:
		break;
