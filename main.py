"""
Reverse words
https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/python
Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained.
Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words_1(text):
    return ' '.join(i[::-1] for i in text.split(' '))


def reverse_words_2(text):
    r = text
    x = []
    while len(r) > 0:
        l, c, r = r.partition(' ')
        if l != ' ':
            x.append(l[::-1] + ' ')
        else:
            x.append(' ')
        # print("[{}] [{}] [{}]".format(l, c, r))
        # print(x)
    return ''.join(x).strip()


if __name__ == '__main__':
    print(reverse_words_1("sihT si na !elpmaxe"))
    print(reverse_words_1("elbuod  secaps"))
    print(reverse_words_1("double  spaced  words"))

    # import timeit
    # print(min(timeit.repeat(stmt=reverse_words, number=10, repeat=5)))  #
