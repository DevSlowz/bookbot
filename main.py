
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def string_to_total_words(book_content):
    word_count = book_content.split()
    return len(word_count)

def main():
    result = get_book_text("./books/frankenstein.txt")
    num_words = string_to_total_words(result)
    print(f"{num_words} words found in the document")


main()