# time: O(s2+s1)
# space: O(s1)

import sys


def main(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        h = set(list(s1))
        print(h)
        for char in s2:
            if char not in h:
                return False
        return True


if __name__ == '__main__':
    print(main(sys.argv[1], sys.argv[2]))
