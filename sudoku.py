def read_sudoku(file_name):
    with open(file_name, 'r') as file:
        size = int(file.readline())
        puzzle = [[0] * size for _ in range(size)] #creates an empty puzzle of size x size
        for i in range(size):
            puzzle[i] = list(map(int, file.readline().split()))
    return puzzle

def write_solution(file_name, solution):
    with open("Solution.txt", 'w') as file:
        if solution:
            for row in solution:
                file.write(' '.join(map(str, row)) + '\n')
        else:
            file.write("No solution exists.")

def is_safe(puzzle, row, col, num):
    size = len(puzzle)

    #Check if the number is already used in the row
    if num in puzzle[row]:
        return False
    
    #Check if the number is already used in the column
    for i in range(size):
        if puzzle[i][col] == num:
            return False
        
    #Check if the number is already used in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if puzzle[i + start_row][j + start_col] == num:
                return False
    return True

def find_empty_location(puzzle):
    size = len(puzzle)
    for i in range(size):
        for j in range(size):
            if puzzle[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(puzzle):
    empty_location = find_empty_location(puzzle)
    if not empty_location:
        return puzzle
    row, col = empty_location
    for num in range(1, len(puzzle) + 1): #numbers in range 1-size of puzzle
        if is_safe(puzzle, row, col, num):
            puzzle[row][col] = num
            if solve_sudoku(puzzle):
                return puzzle
            puzzle[row][col] = 0
    return None

def main(input_file):
    puzzle = read_sudoku(input_file)
    solution = solve_sudoku(puzzle)
    write_solution(input_file, solution)

if __name__ == "__main__":
    main("input.txt")
