def get_num_words(book_content):
    word_count = book_content.split()
    return len(word_count)



def get_character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
        
def sort_on(dict):
    return dict["count"]

def demo(dict_characters):
    results = []

    for entry in dict_characters:
        results.append({"character":entry, "count":dict_characters[entry]})

    results.sort(reverse=True, key=sort_on)

    return results


def print_results(list):
    print("--------- Character Count -------")
    for item in list:
        if item['character'].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")
        

# def sort_on(dict):
#     return dict[]