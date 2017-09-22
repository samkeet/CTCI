def main(mat):
	l = len(mat[0])
	for i in range(l):
		for j in range(l):
			if i == 0 or j == 0 and mat[i][j] == 0:
				set_0(i,j)
			elif mat[i][j] == 0 and mat[i][j-1] != 0 and mat[i-1][j] != 0:
				pass


if __name__ == '__main__':
	main()