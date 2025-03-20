def count_words(text):
    num = len(text.split())
    _str = f"Found {num} total words"#f"{num} words found in the document"

    return _str

def count_characters(text):
    char_dict ={}

    for char in text:
        low_char = char.lower()
        if(char.isalpha() == False):
            pass
        elif(low_char not in char_dict):
            char_dict[low_char] = 1
        else:
            char_dict[low_char] += 1
        
    return char_dict

def sort_on(dict):
    return dict["count"]

def to_sort(dict):
    new_list = []

    for entry in dict:
        new_dict ={}
        new_dict["char"] = entry
        new_dict["count"] = dict[entry]

        new_list.append(new_dict)

    new_list.sort(reverse=True, key=sort_on)

    #print(new_list)
    return new_list