"""Generate Markov text from text files."""

from random import choice
import sys
print(sys.argv)

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()
    

    return file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    text_words = text_string.split()

    chains = {}

    #count
    count = 0
    #while loop over each word
    while count < len(text_words) - 2:
        key = (text_words[count], text_words[count+1])
        value = text_words[count+2]

        if key not in chains:
            chains[key] = []
        
        chains[key].append(value)
        
        count += 1

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # start = choice(list(chains.keys()))
    # while True:
    #     if start[0][0] >= "A" and start[0][0] <= "Z":
    #         words.append(start[0])
    #         words.append(start[1])
    #         break
    #     else:
    #         start = choice(list(chains.keys()))

    cap_alpha = set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
        "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
    

    start = choice(list(chains.keys()))
    while True:
        if start[0][0] in cap_alpha:
            words.append(start[0])
            words.append(start[1])
            break
        else:
            start = choice(list(chains.keys()))

    #loop to get keys
    while True:
        try:
            key = (words[-2], words[-1])
            next_word = choice(chains[key])
            words.append(next_word)
        except KeyError:
            break

        #choice for 3rd word
        #find 2nd and 3rd word as key in dict
        #choice for 4th word
        #loop

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
