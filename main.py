def main():
    book_path = "books/frankenstein.txt"    # filsti
    text = get_book_text(book_path)         # hente test fra filsti
    print(text)                             #Printe/vis text fra fil/bok

def get_book_text(path):    # Finn bok fra filsti
    with open(path) as f:   # Gjør noe med f (filen) fra filsti her
        return f.read()     # Les filen
    
main()