def grabcolumn(line):
	if "\t" in line:
		splitline = line.split("\t")
		return splitline[1]
	else:
		raise Exception()

with open("ja-ud.conllu") as file:
	i = 0
	for line in file.readlines():
		try: 
			column =  grabcolumn(line)
			print(column)
		except:
			pass
		i = 1 + 1
		if i > 800:
			break;
