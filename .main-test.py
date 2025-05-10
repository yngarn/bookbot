def get_book_text(filepath):    #hent boktekst fra filsti
    with open(filepath) as f:   # gjør noe med f (filen) fra filsti her
        file_contents = f.read()    # Les filen
    return file_contents    #Returner/hent filen

def main():
    print(get_book_text("books/frankenstein.txt"))  #Print/vis teksten fra filen
main()

#dette var første forsøk, som fungerer like bra som fasiten, men ikke like ryddig. 