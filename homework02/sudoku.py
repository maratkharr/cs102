import random
import time


def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [values[n*i:n*i+n] for i in range(n)]


def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row, col = pos
    return values[row]


def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    row, col = pos
    """
    col_items = []
    for i in range(len(values)):
        col_items.append(values[i][col])
    return col_items
    """
    return [values[i][col] for i in range(len(values))]


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos
    block_items = []

    st_row = row // 3 * 3
    st_col = col // 3 * 3

    for i in range(st_row, st_row + 3):
        for j in range(st_col, st_col + 3):
            block_items.append(values[i][j])

    return block_items


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    empty_position = ()
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == ".":
                return (i, j)

    return (-1, -1)


def find_possible_values(grid, pos):
    """ Вернуть все возможные значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> set(values) == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> set(values) == {'2', '5', '9'}
    True
    """
    possible_values = []
    possible_row = get_row(grid, pos)
    possible_col = get_col(grid, pos)
    possible_block = get_block(grid, pos)
    for i in range(1, 10):
        if (str(i) not in possible_row and
            str(i) not in possible_col and
            str(i) not in possible_block):
            possible_values.append(str(i))
    return possible_values


def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    """
    empty_position = find_empty_positions(grid)

    if empty_position == (-1, -1):
        return grid

    possible_values = find_possible_values(grid, empty_position)

    if not len(possible_values):
        return

    col, row = empty_position
    for i in possible_values:
        grid[col][row] = i
        solution = solve(grid)
        if solution:
            return grid

    grid[col][row] = '.'


def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """
    correct_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    ans = True

    for i in range(9):
        for j in range(9):
            cur_row = get_row(solution, (i, j))
            cur_col = get_col(solution, (i, j))
            cur_block = get_block(solution, (i, j))
            cur_row.sort()
            cur_col.sort()
            cur_block.sort()
            if not (cur_row == cur_col == cur_block == correct_list):
                ans = False
    return ans


def generate_sudoku(N):
    """ Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    40
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    N = 81 - N
    grid = []
    for i in range(9):
        cur_row = []
        for j in range(9):
            cur_row.append('.')
        grid.append(cur_row)

    grid = solve(grid)

    while N != 0:
        N -= 1
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        while (grid[x][y] == '.'):
            x = random.randint(0, 8)
            y = random.randint(0, 8)

        grid[x][y] = '.'

    return grid

if __name__ == '__main__':
    for fname in ('Puzzle1.txt', 'Puzzle2.txt', 'Puzzle3.txt'):
        grid = read_sudoku(fname)
        start = time.time()
        solve(grid)
        end = time.time()
        print(fname + ": " + str(end - start))
