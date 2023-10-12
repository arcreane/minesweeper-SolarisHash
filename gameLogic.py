import os
import random
from re import U


def set_difficulty():
    check_digit = True
    while check_digit:
        try:
            print("Choose your difficulty")
            difficulty = int(input("1.Easy\t2.Medium\t3.Hard\t4.Personnalisé\n"))
            match difficulty:
                case 1:
                    return 9, 9, 10
                case 2:
                    return 16, 16, 40
                case 3:
                    return 30, 16, 99
                case 4:
                    x = int(input("Enter field height: "))
                    y = int(input("Enter field width: "))
                    mines = int(input("Enter mines number: "))
                    return y, x, mines

        except ValueError:
            print("Choose a right choice")


def create_grid(width, height, mines):
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    grid_for_game = [["\u2588" for _ in range(width)] for _ in range(height)]
    put_mine(grid, mines)
    put_indicate(grid)
    return grid, grid_for_game


def put_mine(grid, mines):
    width = len(grid[0])
    height = len(grid)
    mine_put = 0

    while mine_put < mines:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        if grid[y][x] != '*':
            grid[y][x] = '*'
            mine_put += 1


def put_flag(grid_for_game, x, y):
    if grid_for_game[y][x] == '\u25B2':
        print("Case already discovered")
        return

    grid_for_game[y][x] = '\u25B2'


def put_indicate(grid):
    width = len(grid[0])
    height = len(grid)

    for y in range(height):
        for x in range(width):
            if grid[y][x] == ' ':
                adjacent_mines = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= x + dx < width and 0 <= y + dy < height:
                            if grid[y + dy][x + dx] == '*':
                                adjacent_mines += 1
                if adjacent_mines > 0:
                    grid[y][x] = str(adjacent_mines)


def display_grid(grid):
    width = len(grid[0])
    height = len(grid)

    for row in range(height):
        print(f'{row:2} ', end='')

        for col in range(width):
            if col < 10:
                print(f' {grid[row][col]} ', end='')
            else:
                print(f' {grid[row][col]:2} ', end='')

        print()

        # Afficher les numéros de colonne en bas
    print('   ', end='')
    for col in range(width):
        if col < 10:
            print(f' {col} ', end='')
        else:
            print(f' {col:2} ', end='')

    print('\n')


def display_grid2(grid, grid_for_game):
    width = len(grid[0])
    height = len(grid)

    for row in range(height):
        print(f'{row:2} ', end='')

        for col in range(width):
            if grid_for_game[row][col] == "\u2588":
                print(' {:2} '.format("\u2588"), end='')
            elif grid_for_game[row][col] == '\u25B2':
                print(' {:2} '.format("\u25B2"), end='')
            else:
                print(f' {grid[row][col]:2} ', end='')

        print()

        # Afficher les numéros de colonne en bas
    print('   ', end='')
    for col in range(width):
        if col < 10:
            print(f' {col:2} ', end='')
        else:
            print(f' {col:2} ', end='')

    print('\n')


def decouvrir_case(grid, grid_for_game, x, y, cells_without_mines):
    width = len(grid[0])
    height = len(grid)

    if grid_for_game[y][x] == ' ':
        return

    if grid_for_game[y][x] == 'F':
        return

    grid_for_game[y][x] = ' '

    if grid[y][x] == ' ':
        cells_without_mines -= 1

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < width and 0 <= y + dy < height:
                    decouvrir_case(grid, grid_for_game, x + dx, y + dy, cells_without_mines)

def count_discovered_cells(grid_for_game):
    discovered_cells = 0

    for row in grid_for_game:
        discovered_cells += row.count(' ')

    return discovered_cells