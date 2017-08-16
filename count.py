"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2

    >>> word_count("berry berry cherry cherry berry apple")
    apple: 1
    cherry: 2
    berry: 3

"""


def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""

    def count_words(phrase):

        counts = {}

        phrase = phrase.split(" ")

        for word in phrase:
            if counts.get(word, 0) == 0:
                counts[word] = 1
            else:
                counts[word] += 1

        return counts

    def print_sorted(counts):

        printable = []
        for k, v in counts.items():
            k, v = v, k
            printable.append((k, v))
        printable.sort()

        for item in printable:
            print item[1] + ": " + str(item[0])

    print_sorted(count_words(phrase))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"
