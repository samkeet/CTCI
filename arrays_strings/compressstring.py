import sys


def main(s):
    l = len(s)
    res = []
    i = 0
    while i < l-1:
        j = 1
        while (i < l-1 and s[i] == s[i+1]):
            i += 1
            j += 1
        res.append(s[i])
        res.append(str(j))
        i += 1

    if len(res) >= len(s):
        return s
    else:
        return ''.join(res)


if __name__ == '__main__':
    print(main(sys.argv[1]))