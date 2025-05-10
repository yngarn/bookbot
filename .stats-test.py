def get_num_words(text):
    words = text.split()    # Deler opp ordene i setningene
    return len(words)

def get_chars_dict(text):
    character = {}
    count = len(character)
    for c in text:
        if c.lower() in character:
            character[c.lower()] += 1
            count += 1
        else: 
            character[c.lower()] = 1
            count = 1
    return character, count