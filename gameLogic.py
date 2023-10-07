import os
import random
from re import U


def set_difficulty():
    check_digit = True
    while check_digit:
        try:
            print("Choose your difficulty")
            difficulty = int(input("1.Easy\t2.Medium\t3.Hard\n"))
            match difficulty:
                case 1:
                    return 9, 9, 10
                case 2:
                    return 16, 16, 40
                case 3:
                    return 30, 16, 99
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
    largeur = len(grid[0])
    hauteur = len(grid)

    for row in range(hauteur):
        print(f'{row:2} ', end='')

        for col in range(largeur):
            if col < 10:
                print(f' {grid[row][col]} ', end='')
            else:
                print(f' {grid[row][col]:2} ', end='')

        print()

        # Afficher les numéros de colonne en bas
    print('   ', end='')
    for col in range(largeur):
        if col < 10:
            print(f' {col} ', end='')
        else:
            print(f' {col:2} ', end='')

    print('\n')


def display_grid2(grid, grid_for_game):
    largeur = len(grid[0])
    hauteur = len(grid)

    for row in range(hauteur):
        print(f'{row:2} ', end='')

        for col in range(largeur):
            if grid_for_game[row][col] == "\u2588":
                print(' {:2} '.format("\u2588"), end='')
            else:
                print(f' {grid[row][col]:2} ', end='')

        print()

        # Afficher les numéros de colonne en bas
    print('   ', end='')
    for col in range(largeur):
        if col < 10:
            print(f' {col:2} ', end='')
        else:
            print(f' {col:2} ', end='')

    print('\n')

def decouvrir_case(grid, etat_plateau, x, y):
    width = len(grid[0])
    height = len(grid)

    if etat_plateau[y][x] == ' ':
        return

    etat_plateau[y][x] = ' '

    if grid[y][x] == ' ':

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < width and 0 <= y + dy < height:
                    decouvrir_case(grid, etat_plateau, x + dx, y + dy)

