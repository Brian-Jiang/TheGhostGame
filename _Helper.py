import re

def find_prefix(prefix, words):
    pattern = re.compile(prefix + '[A-z]')
    result = set()
    for word in words:
        if pattern.match(word):
            result.add(word.rstrip('\n'))
    return result


if __name__ == '__main__':
    reader = open('dictionary.txt', 'r')
    words = set(reader.readlines())
    r = find_prefix('aaa', words)
    print(r)