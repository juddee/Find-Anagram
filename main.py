# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if (sorted(word) == sorted(anagram)):
        print(word , ' and ' , anagram, ' are anagrams')
        return True
    else:
        print(word , ' and ' , anagram, ' are not anagrams')
        return False


find_anagram("below", "elbow")
find_anagram("hello", "check")
