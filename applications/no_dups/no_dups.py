def no_dups(s):
    # Your code here
    cache = {}
    strs = s.split()

    for c in strs:
        if c not in cache:
            cache[c] = 1
        else:
            cache[c] += 1
    cache.keys()

    str1 = " "
    list_a = list(cache.keys())
    print(list_a)

    return str1.join(list_a)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
