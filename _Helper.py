import re


def find_prefix(prefix, words):
    pattern = re.compile(prefix + '[A-z]')
    result = set()
    for word in words:
        if pattern.match(word):
            result.add(word.rstrip('\n'))
    return result


def get_word_bank():
    reader = open('dictionary.txt', 'r')
    words = set(reader.readlines())
    return words


if __name__ == '__main__':
    pass
    # reader = open('dictionary.txt', 'r')
    # words = set(reader.readlines())
    # r = find_prefix('aaa', words)
    # print(r)