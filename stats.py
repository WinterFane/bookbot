def count_words(text):
    num = len(text.split())
    _str = f"{num} words found in the document"

    return _str

def count_characters(text):
    char_dict ={}

    for char in text:
        low_char = char.lower()
        if(low_char not in char_dict):
            char_dict[low_char] = 1
        else:
            char_dict[low_char] += 1
        
    return char_dict