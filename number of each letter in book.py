#return the number of each letter in the book
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

def reverse ():
	inverse = {}
	d = count_letter("book.txt")
	for key in d:
		val = d[key]
		if val in inverse:
			inverse[val].append[key]
		else:
			inverse[val] = [key]
	return inverse

print (reverse())
