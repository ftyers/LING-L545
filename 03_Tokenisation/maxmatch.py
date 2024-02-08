def maxMatch(sentence, dictionary):
	if sentence == "":
		return []
	for i,character in enumerate(sentence): 
		firstword = sentence[:i]
		remainder = sentence[i:]
		if firstword in dictionary:
			return list(fistword, maxMatch(remainder, dictionary))

	firstword = sentence[0]
	remainder = sentence[1:]
	return list(firstword, maxMatch(remainder, dictionary))
