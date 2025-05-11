from stats import (
    get_num_words, 
    get_chars_dict, 
    chars__dict_to_sorted_list,      # Importerer fra stats.py
)


def main():
    book_path = "books/frankenstein.txt"            # Filsti
    text = get_book_text(book_path)                 # Hente test fra filsti
    num_words = get_num_words(text)                 # Teller ordene
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars__dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):    # Finn bok fra filsti
    with open(path) as f:   # Gjør noe med f (filen) fra filsti her
        return f.read()     # Les filen
    
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")    # Filsti
    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")             # Teller ord
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():                  # Sorterer bokstavene alfabetisk
            continue
        print(f"{item['char']}: {item['num']}")                  

    print("============= END ===============")


main()
