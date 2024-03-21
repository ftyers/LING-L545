import sys

def grabcolumn(line):
	if "\t" in line:
		splitline = line.split("\t")
		return splitline[1]
	else:
		raise Exception()

with open("ja-ud.conllu") as file:
	out = []
	for line in file.readlines():
		try: 
			column =  grabcolumn(line)
			out.append(column)
		except:
			pass
	print(out)
