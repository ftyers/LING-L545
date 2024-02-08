import sys

line = sys.stdin.readline()

with open("abbreviations.txt") as file:
    abbreviations = []
    for item in file.readlines():
        abbreviations.append(line)
    abbreviations = set(abbreviations)

with open("cleanLinesEncoding.txt") as file:
	for item in file.readlines():
		for token in item.strip().split(' '):
			if not token:
				continue
			if token in abbreviations:
				sys.stdout.write(token + '\n')
			elif token[-1] == '.':
				if token in abbreviations:
					sys.stdout.write(token + ' ')
				else: 
					sys.stdout.write(token + '\n')
			else:
				sys.stdout.write(token + ' ')
