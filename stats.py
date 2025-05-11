def get_num_words(text):
    words = text.split()            # Deler opp ordene i setningene
    return len(words)               # Teller ordene

def get_chars_dict(text):
    chars = {}                      # Lister opp alle unike tegn
    for c in text:                  # Alle karakterer (c) i ord (text)
        lowered = c.lower()         # Gjør alle bokstavene små
        if lowered in chars:
            chars[lowered] += 1     # Hvis ordet finnes i listen, +1
        else: 
            chars[lowered] = 1      # Hvis ordet ikke finnes, legge det til
    return chars

def sort_on(d):
    return d["num"]
    
def chars__dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char, count in chars_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)               # Sorterer på key, som i dette tilfellet er "num" i sort_on funksjonen. 
    return sorted_list

