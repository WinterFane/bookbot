import sys

from stats import count_words,count_characters,to_sort

def get_book_text(filepath):
    _str = ""

    with open(filepath) as file:
        _str = file.read()

    return _str
    #return ''

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1];

    book = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(count_words(book))
    print("--------- Character Count -------")
    to_print = to_sort(count_characters(book))
    for entry in to_print:
        print(f"{entry["char"]}: {entry["count"]}")


main()