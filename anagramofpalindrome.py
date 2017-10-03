"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

    >>> is_anagram_of_palindrome("aaaeeb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letters = [char for char in word]
    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    unmatched_letters = 0
    for value in letter_counts.values():
        if value % 2 != 0:
            unmatched_letters += 1

    # A palindrome will have at most one (the central) unmatched letter.
    return unmatched_letters <= 1


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
