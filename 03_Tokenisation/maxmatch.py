def maxMatch(sentence, dictionary):
	if sentence == "":
		return []
	i = len(sentence)
	while i > 1: 
		firstword = sentence[:i]
		remainder = sentence[i:]
		if firstword in dictionary:
			i -= 1
			return [firstword, maxMatch(remainder, dictionary)]
		i -= 1
	firstword = sentence[0]
	remainder = sentence[1:]
	return [firstword, maxMatch(remainder, dictionary)]

#Get files and contents
sentencesFile = open("original.test.txt", "r")
dictionaryFile = open("dictionary.txt", "r")

sentences = sentencesFile.readlines()
dictionaryWords = dictionaryFile.readlines()

sentencesFile.close()
dictionaryFile.close()

#Stripping new lines from dictionary terms
dictionary = set()
for word in dictionaryWords:
	dictionary.add(word.replace("\n",""))
# Run maxMatch
i = 0
for sentence in sentences:
	temp = maxMatch(sentence.replace(" ", ""), dictionary)
	output = ""
	
	#clear a nasty nested list thing
	while len(temp) == 2:
		output = output + temp[0] + " "
		temp = temp[1]
	print(output, end = "")
