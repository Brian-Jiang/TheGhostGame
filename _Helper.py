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


def check_complete_word(word,words):
    for each in words:
        if word == each[:-1]:
            return True
    return False

if __name__ == '__main__':
    pass
    # reader = open('dictionary.txt', 'r')
    # words = set(reader.readlines())
    # r = find_prefix('aaa', words)
    # print(r)