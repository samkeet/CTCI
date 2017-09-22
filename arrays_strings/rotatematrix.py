def main(mat):
    l = len(mat[0])
    for i in range(l/2):
        for j in range(i, l):
            temp = mat[i][j]
            mat[i][j] = mat[l-j-1][i]
            mat[l-j-1][i] = mat[l-j-1][l-i-1]
            mat[l-j-1][l-i-1] = mat[j][l-i-1]
            mat[j][l-i-1] = temp
    for x in mat:
        print(x)


if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
    main(mat)


# 13,9,5,1
# 14,10,6,2
# 15,11,7,3
# 16,12,8,4
