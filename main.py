def main():
    path_to_file = "books/frankenstein.txt"
    book_text = read_book(path_to_file)
    word_count = count_words(book_text)
    # print(book_text)
    print(word_count)

def read_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words_list = text.split()
    word_count = len(words_list)
    return word_count

main()