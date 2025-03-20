from stats import count_words,count_characters

def get_book_text(filepath):
    _str = ""

    with open(filepath) as file:
        _str = file.read()

    return _str
    #return ''

def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)
    print(count_words(book))
    print(count_characters(book))


#print("asd asd asd".split())
main()