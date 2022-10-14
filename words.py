# 2
def print_upper_words1(words):
    """accept list of words, return one word per line, uppercased"""
    for word in words:
        print(f"{word.upper()}")


# 3
def print_upper_words2(words):
    """accept list of words, return one word per line (uppercased) if word starts with "e", or "E"""""
    for word in words:
        if word[0].upper() == "E":
            print(f"{word.upper()}")


print_upper_words2(["first", "second", "end"])


# 4
def print_upper_words3(words, must_start_with):
    """accepts list of words and options for what the words must start with
    returns one word per line (uppercased) if the first letter of the word is one of the options"""
    for word in words:
        for start_letter in must_start_with:
            if word[0] == start_letter:
                print(f"{word.upper()}")


print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
