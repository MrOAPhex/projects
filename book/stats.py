from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

#testi muuttujat debuggausta varten
tchars = {"a": 6, "b": 8, "c": 2}


vehicles = [
    {"name": "car", "num": 7},
    {"name": "plane", "num": 10},
    {"name": "boat", "num": 2}
]

tx = "HEllo my fellow children"



# iso texti -> sanamäärä
def get_num_words(text):
    ttl = 0
    words = text.split()
    for word in words:
        ttl += 1
    return ttl

# iso teksti -> jokaisen kirjaimen määrä {"a": 6, "b": 7}
def char_count(text):
    ttl = {}
    ltext = text.lower()
    for a in ltext:
        if a in ttl:
            ttl[a] += 1
        else:
            ttl[a] = 1
    return ttl

# ottaa huonosti formatoidun dictin ja tekee siitä järkevän
def dict_sorted(dict: dict[str, int]) -> list[CharacterCount]:
    def sort_on(items):
        return items["num"]
    result: list[CharacterCount] = [] 
    for key in dict:
        result.append({"char": key, "num": dict[key]})
        result.sort(reverse=True, key=sort_on)
    return(result)
 

# print(dict_sorted(tchars))





