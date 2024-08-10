def convert_dict_to_list(dict):
    dict_list = []
    for d in dict:
        if d.isalpha():
            dict_list.append({"char": d, "count": dict[d]})
    return dict_list

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_characters(text):
    char_dict = {}
    for c in text:
        c = c.lower()
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def main():
    text = get_book_text()
    count = word_count(text)
    char_dict = count_characters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print("")
    char_list = convert_dict_to_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    for char in char_list:
        print(f"The '{char['char']}' character was found {char['count']} times")
    print("--- End report ---")

main()
