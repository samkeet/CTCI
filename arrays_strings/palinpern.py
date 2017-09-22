import sys


def odd(s):
    odd_chars = 0
    chars = set(list(s))
    for ch in chars:
        if s.count(ch) % 2 == 0:
            pass
        else:
            odd_chars += 1
            if odd_chars > 1:
                return False
    return True


def even(s):
    chars = set(list(s))
    for ch in chars:
        if s.count(ch) % 2 != 0:
            return False
    return True


def main(s):
    l = len(s)
    if l % 2:
        return odd(s)
    else:
        return even(s)


if __name__ == '__main__':
    print(main(sys.argv[1]))
