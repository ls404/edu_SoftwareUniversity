row_col = input().split()
row_col = [int(row_col[0]), int(row_col[1])]
matrix = []
for i in range(row_col[0]):
    row = input().split()
    matrix.append(row)
row_col = [int(row_col[0])-1, int(row_col[1])-1]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue
    r1, c1, r2, c2 = [int(x) for x in command[1:]]
    if r1 >= 0 and r2 >=0 and c1 >=0 and c2 >=0:
        if r1 <= row_col[0] and r2 <= row_col[0] and c1 <= row_col[1] and c2 <= row_col[1]:
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for i in range(len(matrix)):
                print(' '.join(matrix[i]))
        else:
            print("Invalid input!")
