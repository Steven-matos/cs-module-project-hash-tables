import random
import re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

    cache = {}
    word2 = words.split()
    for i in range(len(word2) - 1):
        if word2[i] not in cache:
            cache[word2[i]] = [word2[i+1]]
        else:
            cache[word2[i]].append(word2[i+1])

    capitalized_words = r"((?:[A-Z][a-z']+)+)"
    endingwords = r"(\w*\.|\w*\?|\w*\!)"

    end = re.findall(endingwords, words)

    cap = re.findall(capitalized_words, words)

    starter = random.choice(cap)

    sentence = starter

    print(starter)

    stop = False
    while stop == False:
        random_word = random.choice(cache[starter])

        if random_word in end:
            sentence += f' {random_word}'
            break
        else:
            sentence += f' {random_word}'
            starter = random_word
    print(sentence)


# TODO: construct 5 random sentences
# Your code here
