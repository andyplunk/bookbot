def count_words (book_text):
	words = book_text.split()
	num_words = 0
	for word in words:
		num_words += 1
	return num_words

def count_chars (book_text):
	book_text = book_text.lower()
	char_counts = {}
	chars = list(book_text)
	for char in chars:
		if char in char_counts:
			char_counts[char] += 1
		else: 
			char_counts[char] = 1
	return char_counts

def sort_list_of_dicts (char_counts):
	list_of_dicts = [{key: value} for key, value in char_counts.items()]
	#sorted_list_of_dicts = list_of_dicts.sort(reverse=True, key=sort_on)
	return [{key: value} for key, value in sorted(char_counts.items(), key=lambda item: item[1], reverse=True)]

	

"""
def count_chars (book_text):
	book_text = book_text.lower()
	char_counts = {}
	chars = list(book_text)
	for char in chars:
		char_counts[char] = char_counts.get(char, 0) + 1
	return char_counts
"""	