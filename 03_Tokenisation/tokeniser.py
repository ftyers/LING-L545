with open("ja-ud.conllu") as file:
	#Grab first line
	currentLine = file.readline()
	
	#If current line contains tab (will contain a surface form), add it to an array. 
	#While the lines have tabs, keep adding the forms to an array
	#Once it returns to a line that doesn't have tabs join the array with a space, and print
	while (currentLine):
		if "\t" in currentLine:
			currentSentence = []
			while "\t" in currentLine:
				currentLine = currentLine.split("\t")
				currentSentence.append(currentLine[1])
				currentLine = file.readline()
			print(" ".join(currentSentence))
		else:
			#move line forward if tab is not in a line
			currentLine = file.readline()

	
