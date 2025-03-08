import sys
from stats import get_num_words, get_character_count,demo,print_results


def get_book_text(path_to_file):


    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def input_validation():
    result = sys.argv
    if len(result) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    return get_book_text(result[1])




def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    result = input_validation()
    num_words = get_num_words(result)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    character_totals = get_character_count(result)



    test = demo(character_totals)
    print_results(test)

main()