import os
import random


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
    put_mine(grid, mines)
    return grid

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


def display_grid(grid):
    #for index, line in enumerate(grid):
        #print(f"{index:>2}",' '.join(line))

    largeur = len(grid[0])
    hauteur = len(grid)
    for row in range(hauteur):
        print(f'{row:2} ', end='')

        for col in range(largeur):
            print(f' {grid[row][col]} ', end='')

        print()

        # Afficher les numéros de colonne en bas
    print('   ', end='')
    for col in range(largeur):
        print(f' {col:2} ', end='')

    print('\n')
