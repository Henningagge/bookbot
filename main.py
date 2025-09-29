from stats import count_words
from stats import count_carackters
import sys as sys
def get_book_text(filepath):
    with open(filepath) as file:
        content = file.read()
    return content
print("Usage: python3 main.py <path_to_book>")

def main(filepath):
    
    words = count_words (filepath)
    carackters = count_carackters(filepath)
    
    carackters = dict(reversed(sorted(carackters.items(), key=lambda item,: item[1])))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for i in carackters:
        print(f"{i}: {carackters[i]}")
main(sys.argv[1])
