from stats import count_words,count_characters,to_sort

def get_book_text(filepath):
    _str = ""

    with open(filepath) as file:
        _str = file.read()

    return _str
    #return ''

def main():
    filepath = "books/frankenstein.txt";

    book = get_book_text(filepath)
    #print(book)
    
    #print(count_characters(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(count_words(book))
    print("--------- Character Count -------")
    to_print = to_sort(count_characters(book))
    for entry in to_print:
        print(f"{entry["char"]}: {entry["count"]}")


#print("asd asd asd".split())
main()