puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    solver(puzzle, 0, 0)
    return puzzle

def next_step(r, c):
    count = 9*r + c
    count += 1
    return count // 9, count % 9

def solver(puzzle, r, c):
    if puzzle[r][c] > 0:
        if r == c == 8:
            return True
        else:
            nr, nc = next_step(r, c)
            return solver(puzzle, nr, nc)
    nums = candidates(puzzle, r, c)
    if len(nums) == 0:
        return False
    if r == c == 8:
        puzzle[r][c] = nums[0]
        return True
    for num in nums:
        nr, nc = next_step(r, c)
        puzzle[r][c] = num
        if solver(puzzle, nr, nc):
            return True
        puzzle[r][c] = 0
    return False

def candidates(puzzle, r, c):
    nums = [True for _ in range(10)]
    # Remove the row numbers
    for num in puzzle[r]:
        nums[num] = False
    # Remove the column numbers
    for i in range(9):
        nums[puzzle[i][c]] = False
    # Remove the block numbers
    blockR = r // 3
    blockC = c // 3
    for br in range(blockR*3, (blockR+1)*3):
        for bc in range(blockC*3, (blockC+1)*3):
            nums[puzzle[br][bc]] = False
    out = []
    for i in range(1, 10):
        if nums[i]:
            out.append(i)
    return out

if __name__ == "__main__":
    print(puzzle)
    print(sudoku(puzzle))
