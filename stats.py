def get_num_words(text):
    words = text.split()            # Deler opp ordene i setningene
    return len(words)               # Teller ordene

def get_chars_dict(text):
    chars = {}                      # Liaster opp alle unike tegn
    for c in text:                  # Alle karakterer (c) i ord (text)
        lowered = c.lower()         # Gjør alle bokstavene små
        if lowered in chars:
            chars[lowered] += 1     # Hvis ordet finnes i listen, +1
        else: 
            chars[lowered] = 1      # Hvis ordet ikke finnes, legge det til
    return chars