from stats import count_words
from stats import count_carackters
def get_book_text(filepath):
    with open(filepath) as file:
        content = file.read()
    return content

def main():
    
    words = count_words ("books/frankenstein.txt")
    carackters = count_carackters("books/frankenstein.txt")
    
    carackters = dict(reversed(sorted(carackters.items(), key=lambda item,: item[1])))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for i in carackters:
        print(f"{i}: {carackters[i]}")
main()