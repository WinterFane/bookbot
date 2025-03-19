def get_book_text(filepath):
    _str = ""

    with open(filepath) as file:
        _str = file.read()

    return _str

def count_words(text):
    

    return 0

def main():
    print(get_book_text("books/frankenstein.txt"))



main()