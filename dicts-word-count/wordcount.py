# open the file
# strip white space from right side of end of lines.
# iterate over lines of file. 
# split lines by ' '
# make empty dict
# iterate over list.
# add words in list to dict.

def get_word_count(file):

    count_of_words = {}

    the_file = open(file)

    for line in the_file:
        line = line.rstrip()
        list_line = line.split(" ")

        for word in list_line:
            count_of_words[word] = count_of_words.get(word, 0) + 1
    return count_of_words


count_of_words = get_word_count("twain.txt")

for key, value in count_of_words.items():
    print(key, value)