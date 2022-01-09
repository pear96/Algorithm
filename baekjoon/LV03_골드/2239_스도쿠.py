MAP = list(list(map(int, input())) for _ in range(9))

rows = list(list(False for _ in range(10)) for _ in range(9))
cols = list(list(False for _ in range(10)) for _ in range(9))
cubes = list(list(False for _ in range(10)) for _ in range(9))

for r in range(9):
    for c in range(9):
        if MAP[r][c]:
            rows[r][MAP[r][c]] = True
            cols[c][MAP[r][c]] = True
            cubes[(r//3)*3+(c//3)][MAP[r][c]] = True


def sudoku(row, col):
    # 마지막까지 왔으면
    if row > 8:
        for line in MAP:
            print("".join(list(map(str, line))))
        exit()
    else:
        # 현재 위치에 숫자가 차 있다면, 다음 자리로 넘어갈 것
        if MAP[row][col]:
            # 다음 줄로 넘어가야 한다면
            if col == 8:
                sudoku(row+1, 0)
            # 다음 열로 넘어가야 한다면
            else:
                sudoku(row, col+1)
        # 현재 위치에 숫자가 비어있다면
        else:
            for number in range(1, 10):
                # 조건에 맞지 않으면
                if not(rows[row][number] or cols[col][number] or cubes[(row//3)*3+(col//3)][number]):
                    # 현재 고른 숫자 표시해주고
                    MAP[row][col] = number
                    rows[row][number], cols[col][number], cubes[(row//3)*3+(col//3)][number] = True, True, True
                    # 다음 위치로 넘어가야 하는데
                    # 다음줄로 넘어가야 한다면
                    if col == 8:
                        sudoku(row + 1, 0)
                    # 다음열로 넘어가야 한다면
                    else:
                        sudoku(row, col + 1)
                    # 완성할 수 없었다면 돌아온 것이므로
                    MAP[row][col] = 0
                    rows[row][number], cols[col][number], cubes[(row//3)*3+(col//3)][number] = False, False, False

sudoku(0, 0)

