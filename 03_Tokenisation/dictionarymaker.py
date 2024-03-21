with open ("tokenised.train.txt") as file:
	words = []
	for line in file.readlines():
		for item in line.split():
			words.append(item)
	words = set(words)
	for word in words:
		print(word) 
