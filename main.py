def get_book_text(filepath):
    _str = ""

    with open(filepath) as file:
        _str = file.read()

    return _str
    #return ''

def count_words(text):
    num = len(text.split())
    _str = f"{num} words found in the document"

    return _str

def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)
    print(count_words(book))


#print("asd asd asd".split())
main()