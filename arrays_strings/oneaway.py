import sys


def main(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    else:
        i, j, missing_char = 0, 0, 0
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        while (i < len(s1) and j < len(s2)):
            if s1[i] != s2[j]:
                missing_char += 1
                if missing_char > 1:
                    return False
            else:






if __name__ == '__main__':
    print(main(sys.argv[1], sys.argv[2]))
