matrix_size = int(input())
valid_pos = [x for x in range(matrix_size)]
matrix = []
pos = []
burrows = []
food_eaten = 0
for i in range(matrix_size):
    row = [_ for _ in input()]
    matrix.append(row)
    if 'S' in row:
        pos.append(i)
        pos.append(row.index('S'))
    if 'B' in row:
        burrows.append([i,row.index('B')])

directions = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0]
}

# print(matrix)
# print(pos)
# print(burrows)

while True:
    command = input()
    matrix[pos[0]][pos[1]] = '.'
    pos[0] += directions[command][0]
    pos[1] += directions[command][1]

    if (pos[0] not in valid_pos) or (pos[1] not in valid_pos):
        print("Game over!")
        print(f"Food eaten: {food_eaten}")
        for _ in range(matrix_size):
            print(''.join(matrix[_]))
        break

    content = matrix[pos[0]][pos[1]]
    # print("content", content)
    if content == '*':
        food_eaten += 1
        if food_eaten < 10:
            matrix[pos[0]][pos[1]] = '.'
        else:
            matrix[pos[0]][pos[1]] = 'S'
    elif content == '-':
        matrix[pos[0]][pos[1]] = '.'

    if content == 'B':
        matrix[pos[0]][pos[1]] = '.'
        # removes current burrow
        # burrows.remove[pos]
        if pos == burrows[0]:
            del burrows[0]
        else:
            del burrows[1]
        # moves to next burrow
        pos[0] = burrows[0][0]
        pos[1] = burrows[0][1]
        matrix[pos[0]][pos[1]] = '.'



    if food_eaten >= 10:
        print("You won! You fed the snake.")
        print(f"Food eaten: {food_eaten}")
        for _ in range(matrix_size):
            print(''.join(matrix[_]))
        break

    # for _ in range(matrix_size):
    #     print(''.join(matrix[_]))
    # print(pos)