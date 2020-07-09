import re


def word_count(s):
    # Your code here

    splits = re.sub('\ |\?|\,|\"|\.|\!|\/|\;|\:', ' ', s)
    counts = {}

    words = splits.split()

    for word in words:
        lower_words = word.lower()
        if lower_words in counts:
            counts[lower_words] += 1
        else:
            counts[lower_words] = 1

    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
