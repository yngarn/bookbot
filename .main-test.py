def get_book_text(filepath):    #hent boktekst fra filsti
    with open(filepath) as f:   # gjør noe med f (filen) fra filsti her
        file_contents = f.read()    # Les filen
    return file_contents    #Returner/hent filen

def main():
    print(get_book_text("books/frankenstein.txt"))  #Print/vis teksten fra filen
main()


print(chars_dict)


 print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")    # Filsti
    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")             # Teller ord
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")                   # Sorterer bokstavene alfabetisk

    print("============= END ===============")


    

main()
#dette var første forsøk, som fungerer like bra som fasiten, men ikke like ryddig. 