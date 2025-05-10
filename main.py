from stats import get_num_words, get_chars_dict          # Importerer fra stats.py


def main():
    book_path = "books/frankenstein.txt"            # Filsti
    text = get_book_text(book_path)                 # Hente test fra filsti
    num_words = get_num_words(text)                 # Teller ordene
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)


def get_book_text(path):    # Finn bok fra filsti
    with open(path) as f:   # Gjør noe med f (filen) fra filsti her
        return f.read()     # Les filen
    

    
main()
