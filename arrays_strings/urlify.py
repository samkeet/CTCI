import sys


def main(s, l):
    char_count = 0
    prev_char = ""
    print(len(s))
    res = []
    for i in range(len(s)):
        if char_count == int(l):
            break
        print(char_count, s[i], prev_char)
        if (s[i] == '_' and i == 0):
            pass
        elif (s[i] == '_'):
            if (prev_char != '_'):
                res.append('%20')
                char_count += 1
        else:
            res.append(s[i])
            char_count += 1
        prev_char = s[i]
    print(''.join(res))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
