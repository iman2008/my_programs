#counting the letter of the book
def count_letter (book):
	with open("book.txt","r") as f:
		dict = {}
		for line in f:
			line = line.split()
			for word in line:
				for letter in word:
					if letter in dict:
						dict[letter]+=1
					else:
						dict[letter]=1
	return (dict)
print (count_letter("book.txt"))
