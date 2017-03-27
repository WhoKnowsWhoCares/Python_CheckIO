def check_pangram(text):
    text = text.lower()
    dict = {}
    for i in text:
        if (i >= 'a' and i <= 'z' and (i not in dict.keys())):
            dict[i] = 1
    print(len(dict))
    if (len(dict.keys()) == 26): return True

    #return set(ascii_lowercase).issubset(set(text.lower()))

    #return not set('abcdefghijklmnopqrstuvwxyz') - set(text.lower())

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
