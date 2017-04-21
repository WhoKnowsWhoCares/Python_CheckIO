def verify_anagrams(first_word, second_word):
    letters = {}
    first_word = first_word.lower().replace(' ','')
    second_word = second_word.lower().replace(' ','')
    for i in first_word:
        if i in letters: letters[i] += 1
        else: letters[i] = 1
    print(letters)
    for i in second_word:
        if i in letters: letters[i] -= 1
        else: return False
    print(letters.values())
    if list(letters.values()).count(0) == len(letters): return True
    return False
	
	#first = [letter from letter in first_word.lower() if letter.isalpha()]
	#second = [letter from letter in second_word.lower() if letter.isalpha()]
	#return sorted(first) == sorted(second)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams('a', 'z'), bool), 'Boolean!'
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"