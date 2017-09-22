# algorithm to find unique characters in string
# time: O(nlog(n))
# space: O(1)
import sys


def isunique(s):
    sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True


if __name__ == '__main__':
    print(isunique(sys.argv[1]))
