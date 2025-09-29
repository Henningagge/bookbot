from stats import count_words
from stats import count_carackters
def get_book_text(filepath):
    with open(filepath) as file:
        content = file.read()
    return content

def main():
    
    
    crackters = count_carackters("books/frankenstein.txt")
    print(crackters)
main()