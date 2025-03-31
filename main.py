import sys

if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

file_path = sys.argv[1]

def get_book_text (file_path):
	book_text = None
	with open(file_path) as f:
		book_text = f.read()
	return book_text

from stats import count_words
from stats import count_chars
from stats import sort_list_of_dicts

def main (file_path):
	book_text = get_book_text(file_path)
	num_words = count_words(book_text)
	char_counts = count_chars(book_text)
	list_of_dicts = sort_list_of_dicts(char_counts)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for entry in list_of_dicts:
		key = list(entry.keys())[0]
		value = entry[key]
		if key.isalpha():
			print(f"{key}: {value}")
	print("============= END ===============")

main(file_path) 
