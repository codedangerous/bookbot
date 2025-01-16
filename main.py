def main():
    path_to_file = "books/frankenstein.txt"
    book_text = read_book(path_to_file)
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    char_counts_list = to_list(char_counts)
    char_counts_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print("")
    for i in range(0, len(char_counts_list)):
        char = char_counts_list[i]["char"]
        count = char_counts_list[i]["count"]
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End Report ---")

def read_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words_list = text.split()
    word_count = len(words_list)
    return word_count

def count_characters(text):
    lowered_string = text.lower()
    char_dict = {}
    for char in lowered_string:
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def to_list(dict):
    new_list = []
    for item in dict:
        new_list.append({"char": item, "count": dict[item]})
    return new_list

def sort_on(dict):
    return dict["count"]


main()