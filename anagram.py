"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, returns the first word with the most anagrams."""

    def is_anagram(word_1, word_2):
        """Given two words, returns True if they are anagrams of one another."""
        return sorted(word_1) == sorted(word_2)

    def get_top_anagram(wordlist):
        """Given a list of words, returns an anagram of the word in the list with
        the most anagrams."""

        counts = {}
        max_count = 0

        for word in wordlist:
            # To find matches, create an anagram of word whose letters are
            # sorted alphabetically: all of word's anagrams, when so treated,
            # will yield the same result, so we can count matches
            base_word = ''.join(sorted(word))
            if base_word in counts.keys():
                counts[base_word] += 1
            else:
                counts[base_word] = 1

            if counts[base_word] > max_count:
                max_count = counts[base_word]
                top_anagram = base_word

        return top_anagram

    top_anagram = get_top_anagram(wordlist)

    for word in wordlist:
        if is_anagram(word, top_anagram):
            return word

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
