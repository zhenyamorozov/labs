VOWELS = "aeiouаеёиоуыэюя"
CONSONANTS = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщъь"

input_string = input("Please, input a string to process: ")

vowels = {}
consonants = {}
others = {}

for c in input_string.lower():
    if c in VOWELS:
        vowels[c] = vowels[c]+1 if c in vowels else 1
    elif c in CONSONANTS:
        consonants[c] = consonants[c]+1 if c in consonants else 1
    else:
        others[c] = others[c]+1 if c in others else 1

vowels = dict(sorted(vowels.items()))
consonants = dict(sorted(consonants.items()))
others = dict(sorted(others.items()))

print(f""" *Frequencies in "{input_string}":*
    Vowels: {vowels.__str__().strip("{}")}
    Consonants: {consonants.__str__().strip("{}")}
    Others: {others.__str__().strip("{}")}
""")